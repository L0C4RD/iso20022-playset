from . import base_types
from ._AdditionalReference10 import AdditionalReference10
from ._Max35Text import Max35Text

class TransferReference14(base_types._BaseFieldType):

	__slots__ = ["_ClntRef", "_CtrPtyRef", "_CxlRef", "_CxlRsn", "_TrfConfRef", "_TrfRef"]
	@property
	def ClntRef(self):
		return self._ClntRef

	@ClntRef.setter
	def ClntRef(self, value):
		self._ClntRef = value if type(value) != base_types.auto else self.make_default("ClntRef")

	@ClntRef.deleter
	def ClntRef(self):
		del self._ClntRef
		self._ClntRef = None

	@property
	def CtrPtyRef(self):
		return self._CtrPtyRef

	@CtrPtyRef.setter
	def CtrPtyRef(self, value):
		self._CtrPtyRef = value if type(value) != base_types.auto else self.make_default("CtrPtyRef")

	@CtrPtyRef.deleter
	def CtrPtyRef(self):
		del self._CtrPtyRef
		self._CtrPtyRef = None

	@property
	def CxlRef(self):
		return self._CxlRef

	@CxlRef.setter
	def CxlRef(self, value):
		self._CxlRef = value if type(value) != base_types.auto else self.make_default("CxlRef")

	@CxlRef.deleter
	def CxlRef(self):
		del self._CxlRef
		self._CxlRef = None

	@property
	def CxlRsn(self):
		return self._CxlRsn

	@CxlRsn.setter
	def CxlRsn(self, value):
		self._CxlRsn = value if type(value) != base_types.auto else self.make_default("CxlRsn")

	@CxlRsn.deleter
	def CxlRsn(self):
		del self._CxlRsn
		self._CxlRsn = None

	@property
	def TrfConfRef(self):
		return self._TrfConfRef

	@TrfConfRef.setter
	def TrfConfRef(self, value):
		self._TrfConfRef = value if type(value) != base_types.auto else self.make_default("TrfConfRef")

	@TrfConfRef.deleter
	def TrfConfRef(self):
		del self._TrfConfRef
		self._TrfConfRef = None

	@property
	def TrfRef(self):
		return self._TrfRef

	@TrfRef.setter
	def TrfRef(self, value):
		self._TrfRef = value if type(value) != base_types.auto else self.make_default("TrfRef")

	@TrfRef.deleter
	def TrfRef(self):
		del self._TrfRef
		self._TrfRef = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClntRef', type=AdditionalReference10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtyRef', type=AdditionalReference10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlRsn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfConfRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfRef', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

