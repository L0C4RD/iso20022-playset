# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection102
from . import GenericIdentification165

class SettlementAccount1(base_types._BaseFieldType):

	__slots__ = ["_EndOfDayDfltFndClld", "_EndOfDayInitlMrgnClld", "_EndOfDayLqdtyClld", "_EndOfDayOthrClld", "_EndOfDaySttlmClld", "_EndOfDayVartnMrgnClld", "_Id"]
	@property
	def EndOfDayDfltFndClld(self):
		return self._EndOfDayDfltFndClld

	@EndOfDayDfltFndClld.setter
	def EndOfDayDfltFndClld(self, value):
		self._EndOfDayDfltFndClld = value if value is not None else base_types.UninitialisedField(self, 'EndOfDayDfltFndClld', AmountAndDirection102, False)

	@EndOfDayDfltFndClld.deleter
	def EndOfDayDfltFndClld(self):
		del self._EndOfDayDfltFndClld
		self._EndOfDayDfltFndClld = base_types.UninitialisedField(self, 'EndOfDayDfltFndClld', AmountAndDirection102, False)

	@property
	def EndOfDayInitlMrgnClld(self):
		return self._EndOfDayInitlMrgnClld

	@EndOfDayInitlMrgnClld.setter
	def EndOfDayInitlMrgnClld(self, value):
		self._EndOfDayInitlMrgnClld = value if value is not None else base_types.UninitialisedField(self, 'EndOfDayInitlMrgnClld', AmountAndDirection102, False)

	@EndOfDayInitlMrgnClld.deleter
	def EndOfDayInitlMrgnClld(self):
		del self._EndOfDayInitlMrgnClld
		self._EndOfDayInitlMrgnClld = base_types.UninitialisedField(self, 'EndOfDayInitlMrgnClld', AmountAndDirection102, False)

	@property
	def EndOfDayLqdtyClld(self):
		return self._EndOfDayLqdtyClld

	@EndOfDayLqdtyClld.setter
	def EndOfDayLqdtyClld(self, value):
		self._EndOfDayLqdtyClld = value if value is not None else base_types.UninitialisedField(self, 'EndOfDayLqdtyClld', AmountAndDirection102, False)

	@EndOfDayLqdtyClld.deleter
	def EndOfDayLqdtyClld(self):
		del self._EndOfDayLqdtyClld
		self._EndOfDayLqdtyClld = base_types.UninitialisedField(self, 'EndOfDayLqdtyClld', AmountAndDirection102, False)

	@property
	def EndOfDayOthrClld(self):
		return self._EndOfDayOthrClld

	@EndOfDayOthrClld.setter
	def EndOfDayOthrClld(self, value):
		self._EndOfDayOthrClld = value if value is not None else base_types.UninitialisedField(self, 'EndOfDayOthrClld', AmountAndDirection102, False)

	@EndOfDayOthrClld.deleter
	def EndOfDayOthrClld(self):
		del self._EndOfDayOthrClld
		self._EndOfDayOthrClld = base_types.UninitialisedField(self, 'EndOfDayOthrClld', AmountAndDirection102, False)

	@property
	def EndOfDaySttlmClld(self):
		return self._EndOfDaySttlmClld

	@EndOfDaySttlmClld.setter
	def EndOfDaySttlmClld(self, value):
		self._EndOfDaySttlmClld = value if value is not None else base_types.UninitialisedField(self, 'EndOfDaySttlmClld', AmountAndDirection102, False)

	@EndOfDaySttlmClld.deleter
	def EndOfDaySttlmClld(self):
		del self._EndOfDaySttlmClld
		self._EndOfDaySttlmClld = base_types.UninitialisedField(self, 'EndOfDaySttlmClld', AmountAndDirection102, False)

	@property
	def EndOfDayVartnMrgnClld(self):
		return self._EndOfDayVartnMrgnClld

	@EndOfDayVartnMrgnClld.setter
	def EndOfDayVartnMrgnClld(self, value):
		self._EndOfDayVartnMrgnClld = value if value is not None else base_types.UninitialisedField(self, 'EndOfDayVartnMrgnClld', AmountAndDirection102, False)

	@EndOfDayVartnMrgnClld.deleter
	def EndOfDayVartnMrgnClld(self):
		del self._EndOfDayVartnMrgnClld
		self._EndOfDayVartnMrgnClld = base_types.UninitialisedField(self, 'EndOfDayVartnMrgnClld', AmountAndDirection102, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', GenericIdentification165, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', GenericIdentification165, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='EndOfDayDfltFndClld', type=AmountAndDirection102, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EndOfDayInitlMrgnClld', type=AmountAndDirection102, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EndOfDayLqdtyClld', type=AmountAndDirection102, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EndOfDayOthrClld', type=AmountAndDirection102, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EndOfDaySttlmClld', type=AmountAndDirection102, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EndOfDayVartnMrgnClld', type=AmountAndDirection102, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=GenericIdentification165, min=1, max=1, mutex_group=None, array=False),
	))