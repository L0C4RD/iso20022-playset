import base_types
import PartyType33Code
import Max35Text
import NetworkParameters7
import Geolocation1
import Min2Max3AlphaText

class GenericIdentification177(base_types._BaseFieldType):

	__slots__ = ["_Ctry", "_Tp", "_Id", "_RmotAccs", "_Glctn", "_ShrtNm", "_Issr"]
	@property
	def Ctry(self):
		return self._Ctry

	@Ctry.setter
	def Ctry(self, value):
		self._Ctry = value if type(value) != auto else self.make_default("Ctry")

	@Ctry.deleter
	def Ctry(self):
		del self._Ctry
		self._Ctry = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def RmotAccs(self):
		return self._RmotAccs

	@RmotAccs.setter
	def RmotAccs(self, value):
		self._RmotAccs = value if type(value) != auto else self.make_default("RmotAccs")

	@RmotAccs.deleter
	def RmotAccs(self):
		del self._RmotAccs
		self._RmotAccs = None

	@property
	def Glctn(self):
		return self._Glctn

	@Glctn.setter
	def Glctn(self, value):
		self._Glctn = value if type(value) != auto else self.make_default("Glctn")

	@Glctn.deleter
	def Glctn(self):
		del self._Glctn
		self._Glctn = None

	@property
	def ShrtNm(self):
		return self._ShrtNm

	@ShrtNm.setter
	def ShrtNm(self, value):
		self._ShrtNm = value if type(value) != auto else self.make_default("ShrtNm")

	@ShrtNm.deleter
	def ShrtNm(self):
		del self._ShrtNm
		self._ShrtNm = None

	@property
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if type(value) != auto else self.make_default("Issr")

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ctry', type=Min2Max3AlphaText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=PartyType33Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmotAccs', type=NetworkParameters7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Glctn', type=Geolocation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrtNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Issr', type=PartyType33Code, min=0, max=1, mutex_group=None, array=False),
	))

