# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CorporateActionNarrative3Choice
from . import Max35Text

class CorporateActionGeneralInformation92(base_types._BaseFieldType):

	__slots__ = ["_CorpActnEvtId", "_NrrtvTp", "_OffclCorpActnEvtId"]
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
	def NrrtvTp(self):
		return self._NrrtvTp

	@NrrtvTp.setter
	def NrrtvTp(self, value):
		self._NrrtvTp = value if value is not None else base_types.UninitialisedField(self, 'NrrtvTp', CorporateActionNarrative3Choice, False)

	@NrrtvTp.deleter
	def NrrtvTp(self):
		del self._NrrtvTp
		self._NrrtvTp = base_types.UninitialisedField(self, 'NrrtvTp', CorporateActionNarrative3Choice, False)

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
		base_types.FieldEntry(name='NrrtvTp', type=CorporateActionNarrative3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OffclCorpActnEvtId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))