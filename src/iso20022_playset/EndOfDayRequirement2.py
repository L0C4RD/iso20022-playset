from . import base_types
import InitialMarginRequirement1
import AmountAndDirection102
import GenericIdentification165

class EndOfDayRequirement2(base_types._BaseFieldType):

	__slots__ = ["_MrgnAcctId", "_VartnMrgnRqrmnts", "_InitlMrgnRqrmnts"]
	@property
	def MrgnAcctId(self):
		return self._MrgnAcctId

	@MrgnAcctId.setter
	def MrgnAcctId(self, value):
		self._MrgnAcctId = value if type(value) != auto else self.make_default("MrgnAcctId")

	@MrgnAcctId.deleter
	def MrgnAcctId(self):
		del self._MrgnAcctId
		self._MrgnAcctId = None

	@property
	def VartnMrgnRqrmnts(self):
		return self._VartnMrgnRqrmnts

	@VartnMrgnRqrmnts.setter
	def VartnMrgnRqrmnts(self, value):
		self._VartnMrgnRqrmnts = value if type(value) != auto else self.make_default("VartnMrgnRqrmnts")

	@VartnMrgnRqrmnts.deleter
	def VartnMrgnRqrmnts(self):
		del self._VartnMrgnRqrmnts
		self._VartnMrgnRqrmnts = None

	@property
	def InitlMrgnRqrmnts(self):
		return self._InitlMrgnRqrmnts

	@InitlMrgnRqrmnts.setter
	def InitlMrgnRqrmnts(self, value):
		self._InitlMrgnRqrmnts = value if type(value) != auto else self.make_default("InitlMrgnRqrmnts")

	@InitlMrgnRqrmnts.deleter
	def InitlMrgnRqrmnts(self):
		del self._InitlMrgnRqrmnts
		self._InitlMrgnRqrmnts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MrgnAcctId', type=GenericIdentification165, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VartnMrgnRqrmnts', type=AmountAndDirection102, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InitlMrgnRqrmnts', type=InitialMarginRequirement1, min=1, max=1, mutex_group=None, array=False),
	))

