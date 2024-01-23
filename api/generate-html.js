// api/generate-html.js

const yourScript = require('./path-to-your-script'); // Adjust path as needed

module.exports = async (req, res) => {
    try {
        // Extract parameters from request
        const { projectId, token } = req.body; // Adjust these parameters based on your script's needs

        // Call your script function
        const htmlContent = await yourScript.generateHtml(projectId, token); // Adjust this line to match how your script works

        // Send the generated HTML back
        res.status(200).send(htmlContent);
    } catch (error) {
        console.error('Error generating HTML:', error);
        res.status(500).send('Error generating HTML');
    }
};
