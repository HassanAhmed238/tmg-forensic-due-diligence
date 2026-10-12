# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

builder_file = r"F:\Mr Hesham\TMG\scripts\build_perfect_dashboard.py"
with open(builder_file, "r", encoding="utf-8") as f:
    text = f.read()

old_block = """    // Initialize Leaflet Map
    function initTmgMap() {
      const mapContainer = document.getElementById('tmg-leaflet-map');
      if (!mapContainer || tmgLeafletMapInstance) return;

      const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
      const tileUrl = isDark 
        ? 'https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png'
        : 'https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png';

      // Center map around Egypt & Regional Expansion
      tmgLeafletMapInstance = L.map('tmg-leaflet-map', {
        center: [28.5, 36.0],
        zoom: 5,
        minZoom: 3,
        maxZoom: 14,
        zoomControl: true
      });

      window.tmgMapTiles = L.tileLayer(tileUrl, {
        attribution: '&copy; OpenStreetMap contributors &copy; CARTO',
        subdomains: 'abcd',
        maxZoom: 19
      }).addTo(tmgLeafletMapInstance);

      // Add Project Markers
      TMG_PROJECTS_MAP.forEach(proj => {
        const isSelected = activeProjectFilter === proj.id;
        const markerColor = proj.color;
        
        // Custom Circle Marker
        const marker = L.circleMarker([proj.lat, proj.lng], {
          radius: 10,
          fillColor: markerColor,
          color: '#ffffff',
          weight: 2,
          opacity: 1,
          fillOpacity: 0.9
        }).addTo(tmgLeafletMapInstance);

        // Tooltip
        marker.bindTooltip(`<strong>${proj.name_ar}</strong><br><span style="font-size:11px; color:#888;">${proj.area}</span>`, {
          permanent: false,
          direction: 'top'
        });

        // Rich Popup
        const popupHtml = `
          <div style="font-family: inherit; min-width: 240px; padding: 4px; color: #111;">
            <div style="display:flex; justify-content:space-between; align-items:center; border-bottom: 2px solid ${proj.color}; padding-bottom: 4px; margin-bottom: 6px;">
              <h4 style="margin:0; font-size:14px; font-weight:800; color:#111827;">${proj.name_ar}</h4>
            </div>
            <div style="font-size:12px; margin-bottom:4px;">📍 <strong>الموقع:</strong> ${proj.location_ar}</div>
            <div style="font-size:12px; margin-bottom:4px;">📐 <strong>المساحة:</strong> ${proj.area}</div>
            <div style="font-size:12px; margin-bottom:4px;">💰 <strong>القيمة / الأثر:</strong> ${proj.gdv}</div>
            <div style="font-size:12px; margin-bottom:6px;">🏗️ <strong>المقاولون الرئيسيون:</strong> ${proj.contractors}</div>
            <div style="margin-top:8px;">
              <button onclick="filterMapByProject('${proj.id}')" style="width:100%; background:${proj.color}; color:#fff; border:none; padding:6px 10px; border-radius:6px; font-size:12px; font-weight:700; cursor:pointer;">
                🔍 تصفية الشركات والفرق لهذا المشروع
              </button>
            </div>
          </div>
        `;
        marker.bindPopup(popupHtml);
        tmgMapMarkers[proj.id] = marker;
      });

      window.tmgMapInitialized = true;
    }

    // Switch Map Tile Theme
    function updateMapTheme(theme) {
      if (!tmgLeafletMapInstance || !window.tmgMapTiles) return;
      const tileUrl = theme === 'dark'
        ? 'https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png'
        : 'https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png';
      tmgLeafletMapInstance.removeLayer(window.tmgMapTiles);
      window.tmgMapTiles = L.tileLayer(tileUrl, {
        attribution: '&copy; OpenStreetMap contributors &copy; CARTO',
        subdomains: 'abcd',
        maxZoom: 19
      }).addTo(tmgLeafletMapInstance);
    }"""

new_block = """    // Initialize Leaflet Map
    function initTmgMap() {
      const mapContainer = document.getElementById('tmg-leaflet-map');
      if (!mapContainer || tmgLeafletMapInstance) return;

      const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
      const tileUrl = isDark 
        ? 'https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Dark_Gray_Base/MapServer/tile/{z}/{y}/{x}'
        : 'https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer/tile/{z}/{y}/{x}';

      tmgLeafletMapInstance = L.map('tmg-leaflet-map', {
        center: [27.5, 38.0],
        zoom: 5,
        minZoom: 3,
        maxZoom: 16,
        zoomControl: true
      });

      window.tmgMapTiles = L.tileLayer(tileUrl, {
        attribution: '&copy; Esri, HERE, Garmin, FAO, USGS, EPA',
        maxZoom: 16
      }).addTo(tmgLeafletMapInstance);

      // Add Project Markers with custom HTML Pins & Labels
      const latLngs = [];
      TMG_PROJECTS_MAP.forEach(proj => {
        latLngs.push([proj.lat, proj.lng]);
        
        // Custom Rich HTML DivIcon
        const customIcon = L.divIcon({
          className: 'tmg-map-pin',
          html: `
            <div style="display:flex; flex-direction:column; align-items:center; transform: translate(-50%, -100%); cursor:pointer;">
              <div style="background:${proj.color}; color:#fff; font-weight:800; font-size:11px; padding:3px 8px; border-radius:12px; box-shadow:0 3px 8px rgba(0,0,0,0.35); white-space:nowrap; border:1.5px solid #fff; display:flex; align-items:center; gap:4px;">
                <span>📍</span> <span>${proj.id === 'banan' ? '🇸🇦 بنان الرياض' : (proj.id === 'jood_yamal' ? '🇴🇲 عمان' : proj.name_ar.split(' ')[0] + ' ' + (proj.name_ar.split(' ')[1] || ''))}</span>
              </div>
              <div style="width:10px; height:10px; background:${proj.color}; border:2px solid #fff; border-radius:50%; margin-top:2px; box-shadow:0 0 8px ${proj.color};"></div>
            </div>
          `,
          iconSize: [0, 0],
          iconAnchor: [0, 0]
        });

        const marker = L.marker([proj.lat, proj.lng], { icon: customIcon }).addTo(tmgLeafletMapInstance);

        // Tooltip
        marker.bindTooltip(`<strong>${proj.name_ar}</strong><br><span style="font-size:11px; color:#888;">${proj.area}</span>`, {
          permanent: false,
          direction: 'top'
        });

        // Rich Popup
        const popupHtml = `
          <div style="font-family: inherit; min-width: 250px; padding: 6px; color: #111;">
            <div style="display:flex; justify-content:space-between; align-items:center; border-bottom: 2px solid ${proj.color}; padding-bottom: 5px; margin-bottom: 8px;">
              <h4 style="margin:0; font-size:14px; font-weight:800; color:#111827;">${proj.name_ar}</h4>
            </div>
            <div style="font-size:12px; margin-bottom:5px;">📍 <strong>الموقع:</strong> ${proj.location_ar}</div>
            <div style="font-size:12px; margin-bottom:5px;">📐 <strong>المساحة:</strong> ${proj.area}</div>
            <div style="font-size:12px; margin-bottom:5px;">💰 <strong>القيمة / الأثر:</strong> ${proj.gdv}</div>
            <div style="font-size:12px; margin-bottom:6px;">🏗️ <strong>المقاولون الرئيسيون:</strong> ${proj.contractors}</div>
            <div style="margin-top:10px;">
              <button onclick="filterMapByProject('${proj.id}')" style="width:100%; background:${proj.color}; color:#fff; border:none; padding:7px 12px; border-radius:6px; font-size:12px; font-weight:700; cursor:pointer;">
                🔍 تصفية الشركات والفرق لهذا المشروع
              </button>
            </div>
          </div>
        `;
        marker.bindPopup(popupHtml);
        tmgMapMarkers[proj.id] = marker;
      });

      // Fit bounds to show Egypt, KSA, and Oman
      if (latLngs.length > 0) {
        tmgLeafletMapInstance.fitBounds(latLngs, { padding: [40, 40] });
      }

      window.tmgMapInitialized = true;
    }

    // Switch Map Tile Theme
    function updateMapTheme(theme) {
      if (!tmgLeafletMapInstance || !window.tmgMapTiles) return;
      const tileUrl = theme === 'dark'
        ? 'https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Dark_Gray_Base/MapServer/tile/{z}/{y}/{x}'
        : 'https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer/tile/{z}/{y}/{x}';
      tmgLeafletMapInstance.removeLayer(window.tmgMapTiles);
      window.tmgMapTiles = L.tileLayer(tileUrl, {
        attribution: '&copy; Esri, HERE, Garmin, FAO, USGS, EPA',
        maxZoom: 16
      }).addTo(tmgLeafletMapInstance);
    }"""

if old_block in text:
    text = text.replace(old_block, new_block)
    with open(builder_file, "w", encoding="utf-8") as f:
        f.write(text)
    print("Map styling and tiles successfully upgraded in build_perfect_dashboard.py!")
else:
    print("Target old block not found. Checking snippet:")
    idx = text.find('function initTmgMap')
    print(text[idx:idx+300])
