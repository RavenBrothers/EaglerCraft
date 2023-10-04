const xmlURL = 'https://raw.githubusercontent.com/EaglerDevs/EaglerCraft/main/log4j2.xml';

async function fetchAndDisplayXML() {
    try {
        const response = await fetch(xmlURL);
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const xmlText = await response.text();

       
        const parser = new DOMParser();
        const xmlDoc = parser.parseFromString(xmlText, 'text/xml');


        const xmlContent = document.getElementById('xml-content');
        xmlContent.textContent = xmlDoc.documentElement.textContent;
    } catch (error) {
        console.error('Error:', error);
    }
}

window.addEventListener('load', fetchAndDisplayXML);
