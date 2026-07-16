# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CorporateActionEventType112Choice
from . import CorporateActionMandatoryVoluntary3Choice
from . import Max35Text
from . import NotificationIdentification5

class EventInformation17(base_types._BaseFieldType):

	__slots__ = ["_CorpActnEvtId", "_EvtTp", "_LastNtfctnId", "_MndtryVlntryEvtTp", "_OffclCorpActnEvtId"]
	@property
	def CorpActnEvtId(self):
		return self._CorpActnEvtId

	@CorpActnEvtId.setter
	def CorpActnEvtId(self, value):
		self._CorpActnEvtId = value if value is not None else base_types.UninitialisedField(self, 'CorpActnEvtId', Max35Text, False)

	@CorpActnEvtId.deleter
	def CorpActnEvtId(self):
		del self._CorpActnEvtId
		self._CorpActnEvtId = base_types.UninitialisedField(self, 'CorpActnEvtId', Max35Text, False)

	@property
	def EvtTp(self):
		return self._EvtTp

	@EvtTp.setter
	def EvtTp(self, value):
		self._EvtTp = value if value is not None else base_types.UninitialisedField(self, 'EvtTp', CorporateActionEventType112Choice, False)

	@EvtTp.deleter
	def EvtTp(self):
		del self._EvtTp
		self._EvtTp = base_types.UninitialisedField(self, 'EvtTp', CorporateActionEventType112Choice, False)

	@property
	def LastNtfctnId(self):
		return self._LastNtfctnId

	@LastNtfctnId.setter
	def LastNtfctnId(self, value):
		self._LastNtfctnId = value if value is not None else base_types.UninitialisedField(self, 'LastNtfctnId', NotificationIdentification5, False)

	@LastNtfctnId.deleter
	def LastNtfctnId(self):
		del self._LastNtfctnId
		self._LastNtfctnId = base_types.UninitialisedField(self, 'LastNtfctnId', NotificationIdentification5, False)

	@property
	def MndtryVlntryEvtTp(self):
		return self._MndtryVlntryEvtTp

	@MndtryVlntryEvtTp.setter
	def MndtryVlntryEvtTp(self, value):
		self._MndtryVlntryEvtTp = value if value is not None else base_types.UninitialisedField(self, 'MndtryVlntryEvtTp', CorporateActionMandatoryVoluntary3Choice, False)

	@MndtryVlntryEvtTp.deleter
	def MndtryVlntryEvtTp(self):
		del self._MndtryVlntryEvtTp
		self._MndtryVlntryEvtTp = base_types.UninitialisedField(self, 'MndtryVlntryEvtTp', CorporateActionMandatoryVoluntary3Choice, False)

	@property
	def OffclCorpActnEvtId(self):
		return self._OffclCorpActnEvtId

	@OffclCorpActnEvtId.setter
	def OffclCorpActnEvtId(self, value):
		self._OffclCorpActnEvtId = value if value is not None else base_types.UninitialisedField(self, 'OffclCorpActnEvtId', Max35Text, False)

	@OffclCorpActnEvtId.deleter
	def OffclCorpActnEvtId(self):
		del self._OffclCorpActnEvtId
		self._OffclCorpActnEvtId = base_types.UninitialisedField(self, 'OffclCorpActnEvtId', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CorpActnEvtId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtTp', type=CorporateActionEventType112Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LastNtfctnId', type=NotificationIdentification5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MndtryVlntryEvtTp', type=CorporateActionMandatoryVoluntary3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OffclCorpActnEvtId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))