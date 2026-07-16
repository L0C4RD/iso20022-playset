# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CorporateActionEventType121Choice
from . import CorporateActionMandatoryVoluntary4Choice
from . import RestrictedFINXMax16Text
from . import SecurityIdentification20

class CorporateActionGeneralInformation191(base_types._BaseFieldType):

	__slots__ = ["_ClssActnNb", "_CorpActnEvtId", "_EvtTp", "_FinInstrmId", "_MndtryVlntryEvtTp", "_OffclCorpActnEvtId"]
	@property
	def ClssActnNb(self):
		return self._ClssActnNb

	@ClssActnNb.setter
	def ClssActnNb(self, value):
		self._ClssActnNb = value if value is not None else base_types.UninitialisedField(self, 'ClssActnNb', RestrictedFINXMax16Text, False)

	@ClssActnNb.deleter
	def ClssActnNb(self):
		del self._ClssActnNb
		self._ClssActnNb = base_types.UninitialisedField(self, 'ClssActnNb', RestrictedFINXMax16Text, False)

	@property
	def CorpActnEvtId(self):
		return self._CorpActnEvtId

	@CorpActnEvtId.setter
	def CorpActnEvtId(self, value):
		self._CorpActnEvtId = value if value is not None else base_types.UninitialisedField(self, 'CorpActnEvtId', RestrictedFINXMax16Text, False)

	@CorpActnEvtId.deleter
	def CorpActnEvtId(self):
		del self._CorpActnEvtId
		self._CorpActnEvtId = base_types.UninitialisedField(self, 'CorpActnEvtId', RestrictedFINXMax16Text, False)

	@property
	def EvtTp(self):
		return self._EvtTp

	@EvtTp.setter
	def EvtTp(self, value):
		self._EvtTp = value if value is not None else base_types.UninitialisedField(self, 'EvtTp', CorporateActionEventType121Choice, False)

	@EvtTp.deleter
	def EvtTp(self):
		del self._EvtTp
		self._EvtTp = base_types.UninitialisedField(self, 'EvtTp', CorporateActionEventType121Choice, False)

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification20, False)

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification20, False)

	@property
	def MndtryVlntryEvtTp(self):
		return self._MndtryVlntryEvtTp

	@MndtryVlntryEvtTp.setter
	def MndtryVlntryEvtTp(self, value):
		self._MndtryVlntryEvtTp = value if value is not None else base_types.UninitialisedField(self, 'MndtryVlntryEvtTp', CorporateActionMandatoryVoluntary4Choice, False)

	@MndtryVlntryEvtTp.deleter
	def MndtryVlntryEvtTp(self):
		del self._MndtryVlntryEvtTp
		self._MndtryVlntryEvtTp = base_types.UninitialisedField(self, 'MndtryVlntryEvtTp', CorporateActionMandatoryVoluntary4Choice, False)

	@property
	def OffclCorpActnEvtId(self):
		return self._OffclCorpActnEvtId

	@OffclCorpActnEvtId.setter
	def OffclCorpActnEvtId(self, value):
		self._OffclCorpActnEvtId = value if value is not None else base_types.UninitialisedField(self, 'OffclCorpActnEvtId', RestrictedFINXMax16Text, False)

	@OffclCorpActnEvtId.deleter
	def OffclCorpActnEvtId(self):
		del self._OffclCorpActnEvtId
		self._OffclCorpActnEvtId = base_types.UninitialisedField(self, 'OffclCorpActnEvtId', RestrictedFINXMax16Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClssActnNb', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnEvtId', type=RestrictedFINXMax16Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtTp', type=CorporateActionEventType121Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification20, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MndtryVlntryEvtTp', type=CorporateActionMandatoryVoluntary4Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OffclCorpActnEvtId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=None, array=False),
	))