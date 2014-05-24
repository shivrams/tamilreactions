#!/usr/bin/python
import sys
import getopt
from PIL import Image,ImageDraw,ImageFont
class TextEmbed(object):
	def __init__(self):
		self.shadowcolor="white"
		self.x,self.y=(10,10)
#Open the image
		self.img=Image.open(r"/Users/chaithu/python_programs/pictures/meme.jpg")
#Passing the image size	
		self.width,self.height=(400,400)
#Imaage size variable
		size=(self.width,self.height)
		self.outpath="/Users/chaithu/python_programs/pictures-meme.jpg"	
#Image font size 
		self.fontsize=50
		self.imgfont=ImageFont.truetype(r"/System/Library/Fonts/AppleGothic.ttf",self.fontsize)
#Resizing the image according to the size
		self.imgrs=self.img.resize(size)
		self.Iwidth,self.Iheight=self.imgrs.size
#passing text to the image
		self.addtext=ImageDraw.Draw(self.imgrs)
		self.y=0
		self.offset = 50
		self.opts,self.args = getopt.getopt(sys.argv[1:],"",["top=","topnext=","middle=","middlenext=","bottom=","bottomnext="])
		print "\n\n\n"+str(self.opts)+"\n\n\n"
		self.drawing()
	def textfontcal(self,txt):
		self.text=txt
		print "self.text = %s" %(self.txt)
		self.imgfont=ImageFont.truetype(r"/System/Library/Fonts/AppleGothic.ttf",self.fontsize)
		self.Twidth,self.Theight=self.addtext.textsize(self.text,self.imgfont)
		fontsize=self.fontsize
                while ((self.Twidth > self.Iwidth) | (self.Theight > self.Iheight)):
#                       fontsize=fontsize-2
			fontsize = fontsize - 5 
#selecting the font and size
                        self.imgfont=ImageFont.truetype(r"/System/Library/Fonts/AppleGothic.ttf",fontsize)
# VERY IMPORTANT finding the size of the text on the Image
                        self.Twidth,self.Theight=self.addtext.textsize(self.text,self.imgfont)
                        print ("in while fontsize=%s Twidth=%s Theight=%s Iwidth=%s Iheight=%s" %(fontsize,self.Twidth,self.Theight,self.Iwidth,self.Iheight))
		#return self.txt
	def drawing(self):
		for opt,self.txt  in self.opts:
			if opt == "--top":
				#self.Twidth,self.Theight=self.addtext.textsize(self.txt,self.imgfont)
				#self.textfontcal(self.Twidth,self.Theight)
				self.txt=self.txt.upper()
				self.textfontcal(self.txt)
				self.y = 0
				self.drawn()
				self.offset = self.Theight
				print "self.offest = %s " % (self.offset)
			elif opt ==  "--topnext":
				self.txt=self.txt.upper()
				self.textfontcal(self.txt)
                                self.y =  8 + self.offset 
				self.drawn()
				print "self.offest = %s " % (self.y)
		"""
		elif opt == "--middle":
#			y=0
			Twidth,Theight=addtext.textsize(txt,imgfont)
			y = (2.5*Theight) 
		elif opt == "--middlenext":
#			y=0
			Twidth,Theight=addtext.textsize(txt,imgfont)	
			y = (3.0*Theight)
		elif opt == "--bottom":
#			y=0
			Twidth,Theight=addtext.textsize(txt,imgfont)
			print "BN  "+str(Theight)
			y = Iheight - (2*Theight+10)
		else:
#			y=0
			print "\n\nIN ELSE\n\n"+str(opt)+"\n\n"
			Twidth,Theight=addtext.textsize(txt,imgfont)
			print "B  "+str(Theight)
			y = Iheight - (Theight+20)
			print " Printing from else values Iheight , Theight "+str(Iheight)+" "+str(Theight)
		"""
		self.output()
	def drawn(self):	
		print "PRINTING Y AFTER GETOPTS FOR LLOP"+str(self.y)
		print ("Theigth=%s Twidth=%s" %(self.Theight,self.Twidth))
		print ("Iheigth=%s Iwidth=%s" %(self.Iheight,self.Iwidth))
		self.wtxtpos=0
		self.htxtpos=0
		self.txtpos=(self.wtxtpos,self.htxtpos)
		"""
		while ((Twidth > Iwidth) | (Theight > Iheight)):
#			fontsize=fontsize-2
			fontsize=fontsize-5
#selecting the font and size
			imgfont=ImageFont.truetype(r"/System/Library/Fonts/AppleGothic.ttf",fontsize)
# VERY IMPORTANT finding the size of the text on the Image
			Twidth,Theight=addtext.textsize(txt,imgfont)
			print ("in while fontsize=%s Twidth=%s Theight=%s Iwidth=%s Iheight=%s" %(fontsize,Twidth,Theight,Iwidth,Iheight))
		"""
#		y = Iheight - Theight
		print ("fontsize=%s Twidth=%s Theight=%s Iwidth=%s" %(self.fontsize,self.Twidth,self.Theight,self.Iwidth))
#the logic for the shadow starts
		i,w,z=(0,0,0)
#center computes the midpoint of the image
		center=self.Iwidth/2
		"""
textOS(textOffSet)computes how much the text should be moved from the center
this logic enables the text to the centered on the image
 		"""
		textOS=self.Twidth/2
		print "textOS = %s" %(textOS)
		#y = Iheight - Theight
		for a in range(5):
			i += 0.35
#with variables i,w,z you are giving the boundary(shadow) for the text
			self.addtext.text(((center-textOS)-z, self.y-i), self.txt, font=self.imgfont, fill=self.shadowcolor)
			self.addtext.text(((center-textOS)+w, self.y-i), self.txt, font=self.imgfont, fill=self.shadowcolor)
			self.addtext.text(((center-textOS)-z, self.y+i), self.txt, font=self.imgfont, fill=self.shadowcolor)
			self.addtext.text(((center-textOS)+w, self.y+i), self.txt, font=self.imgfont, fill=self.shadowcolor)
			w +=.5
			z += 0.35
		self.addtext.text(((center-textOS),self.y),self.txt,font=self.imgfont,fill="black")
	def output(self):
		print "printingy == "+str(self.y) 
		self.imgrs.save(self.outpath)
		self.imgrs.show()
	"""
	def textfontcal():
		while ((Twidth > Iwidth) | (Theight > Iheight)):
#                       fontsize=fontsize-2
                        fontsize=fontsize-5
#selecting the font and size
                        imgfont=ImageFont.truetype(r"/System/Library/Fonts/AppleGothic.ttf",fontsize)
# VERY IMPORTANT finding the size of the text on the Image
                        Twidth,Theight=addtext.textsize(txt,imgfont)
                        print ("in while fontsize=%s Twidth=%s Theight=%s Iwidth=%s Iheight=%s" %(fontsize,Twidth,Theight,Iwidth,Iheight))
	"""


T= TextEmbed()
#T.textfontcal()
#T.drawing()











