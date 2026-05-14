# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CorporateActionGeneralInformation195 import CorporateActionGeneralInformation195
from ._CorporateActionOptionStatement1 import CorporateActionOptionStatement1

class CorporateActionDetails1(base_types._BaseFieldType):

	__slots__ = ["_CorpActnGnlInf", "_CorpActnOptn"]
	@property
	def CorpActnGnlInf(self):
		return self._CorpActnGnlInf

	@CorpActnGnlInf.setter
	def CorpActnGnlInf(self, value):
		self._CorpActnGnlInf = value if type(value) != base_types.auto else self.make_default("CorpActnGnlInf")

	@CorpActnGnlInf.deleter
	def CorpActnGnlInf(self):
		del self._CorpActnGnlInf
		self._CorpActnGnlInf = None

	@property
	def CorpActnOptn(self):
		return self._CorpActnOptn

	@CorpActnOptn.setter
	def CorpActnOptn(self, value):
		self._CorpActnOptn = value if type(value) != base_types.auto else self.make_default("CorpActnOptn")

	@CorpActnOptn.deleter
	def CorpActnOptn(self):
		del self._CorpActnOptn
		self._CorpActnOptn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CorpActnGnlInf', type=CorporateActionGeneralInformation195, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnOptn', type=CorporateActionOptionStatement1, min=1, max=1, mutex_group=None, array=False),
	))