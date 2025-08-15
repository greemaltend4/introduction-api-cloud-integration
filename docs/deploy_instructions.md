# Instructions de déploiement

1. Installez AWS CLI et configurez-le avec vos identifiants AWS.
2. Exécutez la commande suivante pour packager votre fonction Lambda:

   ```bash
   aws cloudformation package --template-file template.yaml --s3-bucket YOUR_S3_BUCKET --output-template-file packaged.yaml
   ```

3. Ensuite, déployez la fonction avec:

   ```bash
   aws cloudformation deploy --template-file packaged.yaml --stack-name YOUR_STACK_NAME --capabilities CAPABILITY_IAM
   ```

4. Une fois déployé, vous recevrez l'URL de votre API.
