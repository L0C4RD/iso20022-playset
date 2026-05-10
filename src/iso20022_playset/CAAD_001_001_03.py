from . import base_types
from .BatchManagementInitiationV03 import BatchManagementInitiationV03

class CAAD_001_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_BtchMgmtInitn"]
		@property
		def BtchMgmtInitn(self):
			return self._BtchMgmtInitn

		@BtchMgmtInitn.setter
		def BtchMgmtInitn(self, value):
			self._BtchMgmtInitn = value if type(value) != auto else self.make_default("BtchMgmtInitn")

		@BtchMgmtInitn.deleter
		def BtchMgmtInitn(self):
			del self._BtchMgmtInitn
			self._BtchMgmtInitn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='BtchMgmtInitn', type=BatchManagementInitiationV03, min=1, max=1, mutex_group=None, array=False),
		))

