import base_types
import LimitIdentification3Choice
import Amount4Choice
import Limit10
import Limit8

class LimitStructure5(base_types._BaseFieldType):

	__slots__ = ["_LmtId", "_NewLmtValSet", "_OdLmtValSet", "_LmtValAmdmnt"]
	@property
	def LmtId(self):
		return self._LmtId

	@LmtId.setter
	def LmtId(self, value):
		self._LmtId = value if type(value) != auto else self.make_default("LmtId")

	@LmtId.deleter
	def LmtId(self):
		del self._LmtId
		self._LmtId = None

	@property
	def NewLmtValSet(self):
		return self._NewLmtValSet

	@NewLmtValSet.setter
	def NewLmtValSet(self, value):
		self._NewLmtValSet = value if type(value) != auto else self.make_default("NewLmtValSet")

	@NewLmtValSet.deleter
	def NewLmtValSet(self):
		del self._NewLmtValSet
		self._NewLmtValSet = None

	@property
	def OdLmtValSet(self):
		return self._OdLmtValSet

	@OdLmtValSet.setter
	def OdLmtValSet(self, value):
		self._OdLmtValSet = value if type(value) != auto else self.make_default("OdLmtValSet")

	@OdLmtValSet.deleter
	def OdLmtValSet(self):
		del self._OdLmtValSet
		self._OdLmtValSet = None

	@property
	def LmtValAmdmnt(self):
		return self._LmtValAmdmnt

	@LmtValAmdmnt.setter
	def LmtValAmdmnt(self, value):
		self._LmtValAmdmnt = value if type(value) != auto else self.make_default("LmtValAmdmnt")

	@LmtValAmdmnt.deleter
	def LmtValAmdmnt(self):
		del self._LmtValAmdmnt
		self._LmtValAmdmnt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='LmtId', type=LimitIdentification3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewLmtValSet', type=Limit8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OdLmtValSet', type=Limit10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LmtValAmdmnt', type=Amount4Choice, min=0, max=1, mutex_group=None, array=False),
	))

