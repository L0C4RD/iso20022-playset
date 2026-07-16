# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GenericIdentification48
from . import Max35Binary
from . import Max70Text
from . import POIComponentType7Code
from . import PackageType5
from . import PointOfInteractionComponentAssessment1
from . import PointOfInteractionComponentCharacteristics11
from . import PointOfInteractionComponentIdentification2
from . import PointOfInteractionComponentStatus3

class PointOfInteractionComponent18(base_types._BaseFieldType):

	__slots__ = ["_Assmnt", "_Chrtcs", "_Id", "_Packg", "_PrbVal", "_StdCmplc", "_Sts", "_SubTpInf", "_Tp"]
	@property
	def Assmnt(self):
		return self._Assmnt

	@Assmnt.setter
	def Assmnt(self, value):
		self._Assmnt = value if value is not None else base_types.UninitialisedField(self, 'Assmnt', PointOfInteractionComponentAssessment1, True)

	@Assmnt.deleter
	def Assmnt(self):
		del self._Assmnt
		self._Assmnt = base_types.UninitialisedField(self, 'Assmnt', PointOfInteractionComponentAssessment1, True)

	@property
	def Chrtcs(self):
		return self._Chrtcs

	@Chrtcs.setter
	def Chrtcs(self, value):
		self._Chrtcs = value if value is not None else base_types.UninitialisedField(self, 'Chrtcs', PointOfInteractionComponentCharacteristics11, False)

	@Chrtcs.deleter
	def Chrtcs(self):
		del self._Chrtcs
		self._Chrtcs = base_types.UninitialisedField(self, 'Chrtcs', PointOfInteractionComponentCharacteristics11, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', PointOfInteractionComponentIdentification2, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', PointOfInteractionComponentIdentification2, False)

	@property
	def Packg(self):
		return self._Packg

	@Packg.setter
	def Packg(self, value):
		self._Packg = value if value is not None else base_types.UninitialisedField(self, 'Packg', PackageType5, True)

	@Packg.deleter
	def Packg(self):
		del self._Packg
		self._Packg = base_types.UninitialisedField(self, 'Packg', PackageType5, True)

	@property
	def PrbVal(self):
		return self._PrbVal

	@PrbVal.setter
	def PrbVal(self, value):
		self._PrbVal = value if value is not None else base_types.UninitialisedField(self, 'PrbVal', Max35Binary, False)

	@PrbVal.deleter
	def PrbVal(self):
		del self._PrbVal
		self._PrbVal = base_types.UninitialisedField(self, 'PrbVal', Max35Binary, False)

	@property
	def StdCmplc(self):
		return self._StdCmplc

	@StdCmplc.setter
	def StdCmplc(self, value):
		self._StdCmplc = value if value is not None else base_types.UninitialisedField(self, 'StdCmplc', GenericIdentification48, True)

	@StdCmplc.deleter
	def StdCmplc(self):
		del self._StdCmplc
		self._StdCmplc = base_types.UninitialisedField(self, 'StdCmplc', GenericIdentification48, True)

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if value is not None else base_types.UninitialisedField(self, 'Sts', PointOfInteractionComponentStatus3, False)

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = base_types.UninitialisedField(self, 'Sts', PointOfInteractionComponentStatus3, False)

	@property
	def SubTpInf(self):
		return self._SubTpInf

	@SubTpInf.setter
	def SubTpInf(self, value):
		self._SubTpInf = value if value is not None else base_types.UninitialisedField(self, 'SubTpInf', Max70Text, False)

	@SubTpInf.deleter
	def SubTpInf(self):
		del self._SubTpInf
		self._SubTpInf = base_types.UninitialisedField(self, 'SubTpInf', Max70Text, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', POIComponentType7Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', POIComponentType7Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Assmnt', type=PointOfInteractionComponentAssessment1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Chrtcs', type=PointOfInteractionComponentCharacteristics11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=PointOfInteractionComponentIdentification2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Packg', type=PackageType5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrbVal', type=Max35Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StdCmplc', type=GenericIdentification48, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sts', type=PointOfInteractionComponentStatus3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubTpInf', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=POIComponentType7Code, min=1, max=1, mutex_group=None, array=False),
	))