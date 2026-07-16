# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import RestrictedFINXMax16Text

class CorporateActionEventReference4Choice(base_types._BaseFieldType):

	__slots__ = ["_LkdCorpActnId", "_LkdOffclCorpActnEvtId"]
	@property
	def LkdCorpActnId(self):
		return self._LkdCorpActnId

	@LkdCorpActnId.setter
	def LkdCorpActnId(self, value):
		self._LkdCorpActnId = value if value is not None else base_types.UninitialisedField(self, 'LkdCorpActnId', RestrictedFINXMax16Text, False)

	@LkdCorpActnId.deleter
	def LkdCorpActnId(self):
		del self._LkdCorpActnId
		self._LkdCorpActnId = base_types.UninitialisedField(self, 'LkdCorpActnId', RestrictedFINXMax16Text, False)

	@property
	def LkdOffclCorpActnEvtId(self):
		return self._LkdOffclCorpActnEvtId

	@LkdOffclCorpActnEvtId.setter
	def LkdOffclCorpActnEvtId(self, value):
		self._LkdOffclCorpActnEvtId = value if value is not None else base_types.UninitialisedField(self, 'LkdOffclCorpActnEvtId', RestrictedFINXMax16Text, False)

	@LkdOffclCorpActnEvtId.deleter
	def LkdOffclCorpActnEvtId(self):
		del self._LkdOffclCorpActnEvtId
		self._LkdOffclCorpActnEvtId = base_types.UninitialisedField(self, 'LkdOffclCorpActnEvtId', RestrictedFINXMax16Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='LkdCorpActnId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='LkdOffclCorpActnEvtId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=1, array=False),
	))