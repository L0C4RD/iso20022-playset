from . import base_types
from ._ContentInformationType39 import ContentInformationType39
from ._CryptographicKey18 import CryptographicKey18
from ._DataSetIdentification11 import DataSetIdentification11
from ._Max140Binary import Max140Binary
from ._Max5000Binary import Max5000Binary

class DataSetRequest6(base_types._BaseFieldType):

	__slots__ = ["_DlgtnProof", "_Id", "_POIChllng", "_PrtctdDlgtnProof", "_SsnKey", "_TMChllng"]
	@property
	def DlgtnProof(self):
		return self._DlgtnProof

	@DlgtnProof.setter
	def DlgtnProof(self, value):
		self._DlgtnProof = value if type(value) != base_types.auto else self.make_default("DlgtnProof")

	@DlgtnProof.deleter
	def DlgtnProof(self):
		del self._DlgtnProof
		self._DlgtnProof = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def POIChllng(self):
		return self._POIChllng

	@POIChllng.setter
	def POIChllng(self, value):
		self._POIChllng = value if type(value) != base_types.auto else self.make_default("POIChllng")

	@POIChllng.deleter
	def POIChllng(self):
		del self._POIChllng
		self._POIChllng = None

	@property
	def PrtctdDlgtnProof(self):
		return self._PrtctdDlgtnProof

	@PrtctdDlgtnProof.setter
	def PrtctdDlgtnProof(self, value):
		self._PrtctdDlgtnProof = value if type(value) != base_types.auto else self.make_default("PrtctdDlgtnProof")

	@PrtctdDlgtnProof.deleter
	def PrtctdDlgtnProof(self):
		del self._PrtctdDlgtnProof
		self._PrtctdDlgtnProof = None

	@property
	def SsnKey(self):
		return self._SsnKey

	@SsnKey.setter
	def SsnKey(self, value):
		self._SsnKey = value if type(value) != base_types.auto else self.make_default("SsnKey")

	@SsnKey.deleter
	def SsnKey(self):
		del self._SsnKey
		self._SsnKey = None

	@property
	def TMChllng(self):
		return self._TMChllng

	@TMChllng.setter
	def TMChllng(self, value):
		self._TMChllng = value if type(value) != base_types.auto else self.make_default("TMChllng")

	@TMChllng.deleter
	def TMChllng(self):
		del self._TMChllng
		self._TMChllng = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DlgtnProof', type=Max5000Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=DataSetIdentification11, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='POIChllng', type=Max140Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdDlgtnProof', type=ContentInformationType39, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SsnKey', type=CryptographicKey18, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TMChllng', type=Max140Binary, min=0, max=1, mutex_group=None, array=False),
	))

