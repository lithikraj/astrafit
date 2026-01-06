// Minimal Service Worker
self.addEventListener('install', (e) => {
    e.waitUntil(
        caches.open('astrafit-store').then((cache) => cache.addAll([
            '/static/index.html',
            '/static/manifest.json',
            'https://cdn.tailwindcss.com',
            'https://cdn.jsdelivr.net/npm/chart.js',
            'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css'
        ]))
    );
});

self.addEventListener('fetch', (e) => {
    e.respondWith(
        caches.match(e.request).then((response) => response || fetch(e.request))
    );
});
