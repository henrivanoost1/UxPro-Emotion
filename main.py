from flask import Flask, render_template, Response
from camera import VideoCamera
import time
import subprocess
import cv2
import os
