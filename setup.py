from distutils.core import setup

setup(
    name='mycroft_jarbas_utils',
    version='0.13.2',
    packages=['mycroft_jarbas_utils', 'mycroft_jarbas_utils.ssl',
              'mycroft_jarbas_utils.intent', 'mycroft_jarbas_utils.skills',
              'mycroft_jarbas_utils.browser', 'mycroft_jarbas_utils.phonemes',
              'mycroft_jarbas_utils.messagebus',
              'mycroft_jarbas_utils.clients'],
    install_requires=[
       'langdetect',
       'mtranslate',
       'pronouncing'
    ],
    url='https://github.com/JarbasAl/mycroft_jarbas_utils',
    license='MIT',
    author='JarbasAi',
    author_email='jarbasai@mailfence.com',
    description='mycroft dev tools'
)
