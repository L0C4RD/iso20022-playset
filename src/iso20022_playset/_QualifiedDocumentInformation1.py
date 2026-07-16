# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AlgorithmAndDigest1
from . import BinaryFile1
from . import ExternalDocumentType1Code
from . import ISODate
from . import Max2048Text
from . import Max35Text
from . import Max6Text
from . import YesNoIndicator
from . import xs:ID
from . import xs:IDREF

class QualifiedDocumentInformation1(base_types._BaseFieldType):

	__slots__ = ["_AttchdFile", "_Dgst", "_DocTp", "_Dt", "_ElctrncOrgnl", "_Id", "_Issr", "_ItmIdr", "_ItmListIdr", "_URL", "_Vrsn"]
	@property
	def AttchdFile(self):
		return self._AttchdFile

	@AttchdFile.setter
	def AttchdFile(self, value):
		self._AttchdFile = value if value is not None else base_types.UninitialisedField(self, 'AttchdFile', BinaryFile1, True)

	@AttchdFile.deleter
	def AttchdFile(self):
		del self._AttchdFile
		self._AttchdFile = base_types.UninitialisedField(self, 'AttchdFile', BinaryFile1, True)

	@property
	def Dgst(self):
		return self._Dgst

	@Dgst.setter
	def Dgst(self, value):
		self._Dgst = value if value is not None else base_types.UninitialisedField(self, 'Dgst', AlgorithmAndDigest1, True)

	@Dgst.deleter
	def Dgst(self):
		del self._Dgst
		self._Dgst = base_types.UninitialisedField(self, 'Dgst', AlgorithmAndDigest1, True)

	@property
	def DocTp(self):
		return self._DocTp

	@DocTp.setter
	def DocTp(self, value):
		self._DocTp = value if value is not None else base_types.UninitialisedField(self, 'DocTp', ExternalDocumentType1Code, False)

	@DocTp.deleter
	def DocTp(self):
		del self._DocTp
		self._DocTp = base_types.UninitialisedField(self, 'DocTp', ExternalDocumentType1Code, False)

	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if value is not None else base_types.UninitialisedField(self, 'Dt', ISODate, False)

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = base_types.UninitialisedField(self, 'Dt', ISODate, False)

	@property
	def ElctrncOrgnl(self):
		return self._ElctrncOrgnl

	@ElctrncOrgnl.setter
	def ElctrncOrgnl(self, value):
		self._ElctrncOrgnl = value if value is not None else base_types.UninitialisedField(self, 'ElctrncOrgnl', YesNoIndicator, False)

	@ElctrncOrgnl.deleter
	def ElctrncOrgnl(self):
		del self._ElctrncOrgnl
		self._ElctrncOrgnl = base_types.UninitialisedField(self, 'ElctrncOrgnl', YesNoIndicator, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', xs:ID, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', xs:ID, False)

	@property
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if value is not None else base_types.UninitialisedField(self, 'Issr', xs:IDREF, False)

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = base_types.UninitialisedField(self, 'Issr', xs:IDREF, False)

	@property
	def ItmIdr(self):
		return self._ItmIdr

	@ItmIdr.setter
	def ItmIdr(self, value):
		self._ItmIdr = value if value is not None else base_types.UninitialisedField(self, 'ItmIdr', Max35Text, False)

	@ItmIdr.deleter
	def ItmIdr(self):
		del self._ItmIdr
		self._ItmIdr = base_types.UninitialisedField(self, 'ItmIdr', Max35Text, False)

	@property
	def ItmListIdr(self):
		return self._ItmListIdr

	@ItmListIdr.setter
	def ItmListIdr(self, value):
		self._ItmListIdr = value if value is not None else base_types.UninitialisedField(self, 'ItmListIdr', Max35Text, False)

	@ItmListIdr.deleter
	def ItmListIdr(self):
		del self._ItmListIdr
		self._ItmListIdr = base_types.UninitialisedField(self, 'ItmListIdr', Max35Text, False)

	@property
	def URL(self):
		return self._URL

	@URL.setter
	def URL(self, value):
		self._URL = value if value is not None else base_types.UninitialisedField(self, 'URL', Max2048Text, False)

	@URL.deleter
	def URL(self):
		del self._URL
		self._URL = base_types.UninitialisedField(self, 'URL', Max2048Text, False)

	@property
	def Vrsn(self):
		return self._Vrsn

	@Vrsn.setter
	def Vrsn(self, value):
		self._Vrsn = value if value is not None else base_types.UninitialisedField(self, 'Vrsn', Max6Text, False)

	@Vrsn.deleter
	def Vrsn(self):
		del self._Vrsn
		self._Vrsn = base_types.UninitialisedField(self, 'Vrsn', Max6Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AttchdFile', type=BinaryFile1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Dgst', type=AlgorithmAndDigest1, min=0, max=2, mutex_group=None, array=True),
		base_types.FieldEntry(name='DocTp', type=ExternalDocumentType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ElctrncOrgnl', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=XS_ID, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Issr', type=XS_IDREF, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ItmIdr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ItmListIdr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='URL', type=Max2048Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vrsn', type=Max6Text, min=0, max=1, mutex_group=None, array=False),
	))