from . import base_types
from .Max35Text import Max35Text
from .ExternalDocumentType1Code import ExternalDocumentType1Code
from .YesNoIndicator import YesNoIndicator
from .BinaryFile1 import BinaryFile1
from .ISODate import ISODate
from .Max6Text import Max6Text
from .xs:ID import xs:ID
from .Max2048Text import Max2048Text
from .xs:IDREF import xs:IDREF
from .AlgorithmAndDigest1 import AlgorithmAndDigest1

class QualifiedDocumentInformation1(base_types._BaseFieldType):

	__slots__ = ["_ItmIdr", "_Issr", "_Dgst", "_Id", "_ElctrncOrgnl", "_AttchdFile", "_Dt", "_DocTp", "_URL", "_Vrsn", "_ItmListIdr"]
	@property
	def ItmIdr(self):
		return self._ItmIdr

	@ItmIdr.setter
	def ItmIdr(self, value):
		self._ItmIdr = value if type(value) != auto else self.make_default("ItmIdr")

	@ItmIdr.deleter
	def ItmIdr(self):
		del self._ItmIdr
		self._ItmIdr = None

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

	@property
	def Dgst(self):
		return self._Dgst

	@Dgst.setter
	def Dgst(self, value):
		self._Dgst = value if type(value) != auto else self.make_default("Dgst")

	@Dgst.deleter
	def Dgst(self):
		del self._Dgst
		self._Dgst = None

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
	def ElctrncOrgnl(self):
		return self._ElctrncOrgnl

	@ElctrncOrgnl.setter
	def ElctrncOrgnl(self, value):
		self._ElctrncOrgnl = value if type(value) != auto else self.make_default("ElctrncOrgnl")

	@ElctrncOrgnl.deleter
	def ElctrncOrgnl(self):
		del self._ElctrncOrgnl
		self._ElctrncOrgnl = None

	@property
	def AttchdFile(self):
		return self._AttchdFile

	@AttchdFile.setter
	def AttchdFile(self, value):
		self._AttchdFile = value if type(value) != auto else self.make_default("AttchdFile")

	@AttchdFile.deleter
	def AttchdFile(self):
		del self._AttchdFile
		self._AttchdFile = None

	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if type(value) != auto else self.make_default("Dt")

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = None

	@property
	def DocTp(self):
		return self._DocTp

	@DocTp.setter
	def DocTp(self, value):
		self._DocTp = value if type(value) != auto else self.make_default("DocTp")

	@DocTp.deleter
	def DocTp(self):
		del self._DocTp
		self._DocTp = None

	@property
	def URL(self):
		return self._URL

	@URL.setter
	def URL(self, value):
		self._URL = value if type(value) != auto else self.make_default("URL")

	@URL.deleter
	def URL(self):
		del self._URL
		self._URL = None

	@property
	def Vrsn(self):
		return self._Vrsn

	@Vrsn.setter
	def Vrsn(self, value):
		self._Vrsn = value if type(value) != auto else self.make_default("Vrsn")

	@Vrsn.deleter
	def Vrsn(self):
		del self._Vrsn
		self._Vrsn = None

	@property
	def ItmListIdr(self):
		return self._ItmListIdr

	@ItmListIdr.setter
	def ItmListIdr(self, value):
		self._ItmListIdr = value if type(value) != auto else self.make_default("ItmListIdr")

	@ItmListIdr.deleter
	def ItmListIdr(self):
		del self._ItmListIdr
		self._ItmListIdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ItmIdr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Issr', type=XS_IDREF, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dgst', type=AlgorithmAndDigest1, min=0, max=2, mutex_group=None, array=True),
		base_types.FieldEntry(name='Id', type=XS_ID, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ElctrncOrgnl', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AttchdFile', type=BinaryFile1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Dt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DocTp', type=ExternalDocumentType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='URL', type=Max2048Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vrsn', type=Max6Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ItmListIdr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

