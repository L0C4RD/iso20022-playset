from . import base_types
import AttestationValue1Code
import Exemption2
import Max4Text
import TrueFalseIndicator

class StrongCustomerAuthentication2(base_types._BaseFieldType):

	__slots__ = ["_RsnAuthntcnNotPrfrmd", "_Wvr", "_Xmptn", "_DlgtdAuthrty", "_SbjtToSCA"]
	@property
	def RsnAuthntcnNotPrfrmd(self):
		return self._RsnAuthntcnNotPrfrmd

	@RsnAuthntcnNotPrfrmd.setter
	def RsnAuthntcnNotPrfrmd(self, value):
		self._RsnAuthntcnNotPrfrmd = value if type(value) != auto else self.make_default("RsnAuthntcnNotPrfrmd")

	@RsnAuthntcnNotPrfrmd.deleter
	def RsnAuthntcnNotPrfrmd(self):
		del self._RsnAuthntcnNotPrfrmd
		self._RsnAuthntcnNotPrfrmd = None

	@property
	def Wvr(self):
		return self._Wvr

	@Wvr.setter
	def Wvr(self, value):
		self._Wvr = value if type(value) != auto else self.make_default("Wvr")

	@Wvr.deleter
	def Wvr(self):
		del self._Wvr
		self._Wvr = None

	@property
	def Xmptn(self):
		return self._Xmptn

	@Xmptn.setter
	def Xmptn(self, value):
		self._Xmptn = value if type(value) != auto else self.make_default("Xmptn")

	@Xmptn.deleter
	def Xmptn(self):
		del self._Xmptn
		self._Xmptn = None

	@property
	def DlgtdAuthrty(self):
		return self._DlgtdAuthrty

	@DlgtdAuthrty.setter
	def DlgtdAuthrty(self, value):
		self._DlgtdAuthrty = value if type(value) != auto else self.make_default("DlgtdAuthrty")

	@DlgtdAuthrty.deleter
	def DlgtdAuthrty(self):
		del self._DlgtdAuthrty
		self._DlgtdAuthrty = None

	@property
	def SbjtToSCA(self):
		return self._SbjtToSCA

	@SbjtToSCA.setter
	def SbjtToSCA(self, value):
		self._SbjtToSCA = value if type(value) != auto else self.make_default("SbjtToSCA")

	@SbjtToSCA.deleter
	def SbjtToSCA(self):
		del self._SbjtToSCA
		self._SbjtToSCA = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RsnAuthntcnNotPrfrmd', type=Max4Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Wvr', type=AttestationValue1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Xmptn', type=Exemption2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DlgtdAuthrty', type=AttestationValue1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SbjtToSCA', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
	))

