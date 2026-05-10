import base_types
import AmountAndDirection102
import GenericIdentification165

class SettlementAccount1(base_types._BaseFieldType):

	__slots__ = ["_EndOfDayDfltFndClld", "_EndOfDaySttlmClld", "_EndOfDayOthrClld", "_Id", "_EndOfDayLqdtyClld", "_EndOfDayVartnMrgnClld", "_EndOfDayInitlMrgnClld"]
	@property
	def EndOfDayDfltFndClld(self):
		return self._EndOfDayDfltFndClld

	@EndOfDayDfltFndClld.setter
	def EndOfDayDfltFndClld(self, value):
		self._EndOfDayDfltFndClld = value if type(value) != auto else self.make_default("EndOfDayDfltFndClld")

	@EndOfDayDfltFndClld.deleter
	def EndOfDayDfltFndClld(self):
		del self._EndOfDayDfltFndClld
		self._EndOfDayDfltFndClld = None

	@property
	def EndOfDaySttlmClld(self):
		return self._EndOfDaySttlmClld

	@EndOfDaySttlmClld.setter
	def EndOfDaySttlmClld(self, value):
		self._EndOfDaySttlmClld = value if type(value) != auto else self.make_default("EndOfDaySttlmClld")

	@EndOfDaySttlmClld.deleter
	def EndOfDaySttlmClld(self):
		del self._EndOfDaySttlmClld
		self._EndOfDaySttlmClld = None

	@property
	def EndOfDayOthrClld(self):
		return self._EndOfDayOthrClld

	@EndOfDayOthrClld.setter
	def EndOfDayOthrClld(self, value):
		self._EndOfDayOthrClld = value if type(value) != auto else self.make_default("EndOfDayOthrClld")

	@EndOfDayOthrClld.deleter
	def EndOfDayOthrClld(self):
		del self._EndOfDayOthrClld
		self._EndOfDayOthrClld = None

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
	def EndOfDayLqdtyClld(self):
		return self._EndOfDayLqdtyClld

	@EndOfDayLqdtyClld.setter
	def EndOfDayLqdtyClld(self, value):
		self._EndOfDayLqdtyClld = value if type(value) != auto else self.make_default("EndOfDayLqdtyClld")

	@EndOfDayLqdtyClld.deleter
	def EndOfDayLqdtyClld(self):
		del self._EndOfDayLqdtyClld
		self._EndOfDayLqdtyClld = None

	@property
	def EndOfDayVartnMrgnClld(self):
		return self._EndOfDayVartnMrgnClld

	@EndOfDayVartnMrgnClld.setter
	def EndOfDayVartnMrgnClld(self, value):
		self._EndOfDayVartnMrgnClld = value if type(value) != auto else self.make_default("EndOfDayVartnMrgnClld")

	@EndOfDayVartnMrgnClld.deleter
	def EndOfDayVartnMrgnClld(self):
		del self._EndOfDayVartnMrgnClld
		self._EndOfDayVartnMrgnClld = None

	@property
	def EndOfDayInitlMrgnClld(self):
		return self._EndOfDayInitlMrgnClld

	@EndOfDayInitlMrgnClld.setter
	def EndOfDayInitlMrgnClld(self, value):
		self._EndOfDayInitlMrgnClld = value if type(value) != auto else self.make_default("EndOfDayInitlMrgnClld")

	@EndOfDayInitlMrgnClld.deleter
	def EndOfDayInitlMrgnClld(self):
		del self._EndOfDayInitlMrgnClld
		self._EndOfDayInitlMrgnClld = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='EndOfDayDfltFndClld', type=AmountAndDirection102, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EndOfDaySttlmClld', type=AmountAndDirection102, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EndOfDayOthrClld', type=AmountAndDirection102, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=GenericIdentification165, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EndOfDayLqdtyClld', type=AmountAndDirection102, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EndOfDayVartnMrgnClld', type=AmountAndDirection102, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EndOfDayInitlMrgnClld', type=AmountAndDirection102, min=1, max=1, mutex_group=None, array=False),
	))

