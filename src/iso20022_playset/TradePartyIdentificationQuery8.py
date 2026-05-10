from . import base_types
from .NotReported1Code import NotReported1Code
from .LEIIdentifier import LEIIdentifier
from .AnyBICDec2014Identifier import AnyBICDec2014Identifier
from .Max50Text import Max50Text

class TradePartyIdentificationQuery8(base_types._BaseFieldType):

	__slots__ = ["_ClntId", "_NotRptd", "_LEI", "_AnyBIC"]
	@property
	def ClntId(self):
		return self._ClntId

	@ClntId.setter
	def ClntId(self, value):
		self._ClntId = value if type(value) != base_types.auto else self.make_default("ClntId")

	@ClntId.deleter
	def ClntId(self):
		del self._ClntId
		self._ClntId = None

	@property
	def NotRptd(self):
		return self._NotRptd

	@NotRptd.setter
	def NotRptd(self, value):
		self._NotRptd = value if type(value) != base_types.auto else self.make_default("NotRptd")

	@NotRptd.deleter
	def NotRptd(self):
		del self._NotRptd
		self._NotRptd = None

	@property
	def LEI(self):
		return self._LEI

	@LEI.setter
	def LEI(self, value):
		self._LEI = value if type(value) != base_types.auto else self.make_default("LEI")

	@LEI.deleter
	def LEI(self):
		del self._LEI
		self._LEI = None

	@property
	def AnyBIC(self):
		return self._AnyBIC

	@AnyBIC.setter
	def AnyBIC(self, value):
		self._AnyBIC = value if type(value) != base_types.auto else self.make_default("AnyBIC")

	@AnyBIC.deleter
	def AnyBIC(self):
		del self._AnyBIC
		self._AnyBIC = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClntId', type=Max50Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NotRptd', type=NotReported1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LEI', type=LEIIdentifier, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AnyBIC', type=AnyBICDec2014Identifier, min=0, max=None, mutex_group=None, array=True),
	))

