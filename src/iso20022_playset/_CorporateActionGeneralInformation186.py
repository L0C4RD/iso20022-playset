# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CorporateActionEventType115Choice import CorporateActionEventType115Choice
from ._RestrictedFINXMax16Text import RestrictedFINXMax16Text

class CorporateActionGeneralInformation186(base_types._BaseFieldType):

	__slots__ = ["_ClssActnNb", "_CorpActnEvtId", "_EvtTp", "_OffclCorpActnEvtId"]
	@property
	def ClssActnNb(self):
		return self._ClssActnNb

	@ClssActnNb.setter
	def ClssActnNb(self, value):
		self._ClssActnNb = value if type(value) != base_types.auto else self.make_default("ClssActnNb")

	@ClssActnNb.deleter
	def ClssActnNb(self):
		del self._ClssActnNb
		self._ClssActnNb = None

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
		base_types.FieldEntry(name='ClssActnNb', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnEvtId', type=RestrictedFINXMax16Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtTp', type=CorporateActionEventType115Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OffclCorpActnEvtId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=None, array=False),
	))