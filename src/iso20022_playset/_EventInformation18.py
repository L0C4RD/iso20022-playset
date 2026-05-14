# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CorporateActionEventType117Choice import CorporateActionEventType117Choice
from ._CorporateActionMandatoryVoluntary4Choice import CorporateActionMandatoryVoluntary4Choice
from ._NotificationIdentification6 import NotificationIdentification6
from ._RestrictedFINXMax16Text import RestrictedFINXMax16Text

class EventInformation18(base_types._BaseFieldType):

	__slots__ = ["_CorpActnEvtId", "_EvtTp", "_LastNtfctnId", "_MndtryVlntryEvtTp", "_OffclCorpActnEvtId"]
	@property
	def CorpActnEvtId(self):
		return self._CorpActnEvtId

	@CorpActnEvtId.setter
	def CorpActnEvtId(self, value):
		self._CorpActnEvtId = value if type(value) != base_types.auto else self.make_default("CorpActnEvtId")

	@CorpActnEvtId.deleter
	def CorpActnEvtId(self):
		del self._CorpActnEvtId
		self._CorpActnEvtId = None

	@property
	def EvtTp(self):
		return self._EvtTp

	@EvtTp.setter
	def EvtTp(self, value):
		self._EvtTp = value if type(value) != base_types.auto else self.make_default("EvtTp")

	@EvtTp.deleter
	def EvtTp(self):
		del self._EvtTp
		self._EvtTp = None

	@property
	def LastNtfctnId(self):
		return self._LastNtfctnId

	@LastNtfctnId.setter
	def LastNtfctnId(self, value):
		self._LastNtfctnId = value if type(value) != base_types.auto else self.make_default("LastNtfctnId")

	@LastNtfctnId.deleter
	def LastNtfctnId(self):
		del self._LastNtfctnId
		self._LastNtfctnId = None

	@property
	def MndtryVlntryEvtTp(self):
		return self._MndtryVlntryEvtTp

	@MndtryVlntryEvtTp.setter
	def MndtryVlntryEvtTp(self, value):
		self._MndtryVlntryEvtTp = value if type(value) != base_types.auto else self.make_default("MndtryVlntryEvtTp")

	@MndtryVlntryEvtTp.deleter
	def MndtryVlntryEvtTp(self):
		del self._MndtryVlntryEvtTp
		self._MndtryVlntryEvtTp = None

	@property
	def OffclCorpActnEvtId(self):
		return self._OffclCorpActnEvtId

	@OffclCorpActnEvtId.setter
	def OffclCorpActnEvtId(self, value):
		self._OffclCorpActnEvtId = value if type(value) != base_types.auto else self.make_default("OffclCorpActnEvtId")

	@OffclCorpActnEvtId.deleter
	def OffclCorpActnEvtId(self):
		del self._OffclCorpActnEvtId
		self._OffclCorpActnEvtId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CorpActnEvtId', type=RestrictedFINXMax16Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtTp', type=CorporateActionEventType117Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LastNtfctnId', type=NotificationIdentification6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MndtryVlntryEvtTp', type=CorporateActionMandatoryVoluntary4Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OffclCorpActnEvtId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=None, array=False),
	))