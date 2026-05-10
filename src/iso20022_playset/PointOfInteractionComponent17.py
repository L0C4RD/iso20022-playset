import base_types
import POIComponentType7Code
import Max70Text
import GenericIdentification48
import Max35Binary
import PointOfInteractionComponentAssessment1
import PointOfInteractionComponentCharacteristics10
import PackageType5
import PointOfInteractionComponentIdentification2
import PointOfInteractionComponentStatus3

class PointOfInteractionComponent17(base_types._BaseFieldType):

	__slots__ = ["_PrbVal", "_Sts", "_StdCmplc", "_Chrtcs", "_Id", "_Packg", "_Tp", "_Assmnt", "_SubTpInf"]
	@property
	def PrbVal(self):
		return self._PrbVal

	@PrbVal.setter
	def PrbVal(self, value):
		self._PrbVal = value if type(value) != auto else self.make_default("PrbVal")

	@PrbVal.deleter
	def PrbVal(self):
		del self._PrbVal
		self._PrbVal = None

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if type(value) != auto else self.make_default("Sts")

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = None

	@property
	def StdCmplc(self):
		return self._StdCmplc

	@StdCmplc.setter
	def StdCmplc(self, value):
		self._StdCmplc = value if type(value) != auto else self.make_default("StdCmplc")

	@StdCmplc.deleter
	def StdCmplc(self):
		del self._StdCmplc
		self._StdCmplc = None

	@property
	def Chrtcs(self):
		return self._Chrtcs

	@Chrtcs.setter
	def Chrtcs(self, value):
		self._Chrtcs = value if type(value) != auto else self.make_default("Chrtcs")

	@Chrtcs.deleter
	def Chrtcs(self):
		del self._Chrtcs
		self._Chrtcs = None

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
	def Packg(self):
		return self._Packg

	@Packg.setter
	def Packg(self, value):
		self._Packg = value if type(value) != auto else self.make_default("Packg")

	@Packg.deleter
	def Packg(self):
		del self._Packg
		self._Packg = None

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
	def Assmnt(self):
		return self._Assmnt

	@Assmnt.setter
	def Assmnt(self, value):
		self._Assmnt = value if type(value) != auto else self.make_default("Assmnt")

	@Assmnt.deleter
	def Assmnt(self):
		del self._Assmnt
		self._Assmnt = None

	@property
	def SubTpInf(self):
		return self._SubTpInf

	@SubTpInf.setter
	def SubTpInf(self, value):
		self._SubTpInf = value if type(value) != auto else self.make_default("SubTpInf")

	@SubTpInf.deleter
	def SubTpInf(self):
		del self._SubTpInf
		self._SubTpInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrbVal', type=Max35Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sts', type=PointOfInteractionComponentStatus3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StdCmplc', type=GenericIdentification48, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Chrtcs', type=PointOfInteractionComponentCharacteristics10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=PointOfInteractionComponentIdentification2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Packg', type=PackageType5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Tp', type=POIComponentType7Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Assmnt', type=PointOfInteractionComponentAssessment1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SubTpInf', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
	))

