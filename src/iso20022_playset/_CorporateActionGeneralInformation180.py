# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CorporateActionEventType112Choice import CorporateActionEventType112Choice
from ._FinancialInstrumentAttributes132 import FinancialInstrumentAttributes132
from ._Max35Text import Max35Text

class CorporateActionGeneralInformation180(base_types._BaseFieldType):

	__slots__ = ["_CorpActnEvtId", "_EvtTp", "_OffclCorpActnEvtId", "_UndrlygScty"]
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

	@property
	def UndrlygScty(self):
		return self._UndrlygScty

	@UndrlygScty.setter
	def UndrlygScty(self, value):
		self._UndrlygScty = value if type(value) != base_types.auto else self.make_default("UndrlygScty")

	@UndrlygScty.deleter
	def UndrlygScty(self):
		del self._UndrlygScty
		self._UndrlygScty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CorpActnEvtId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtTp', type=CorporateActionEventType112Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OffclCorpActnEvtId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UndrlygScty', type=FinancialInstrumentAttributes132, min=0, max=1, mutex_group=None, array=False),
	))