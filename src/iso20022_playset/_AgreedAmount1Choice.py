# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AgreedAmount1 import AgreedAmount1
from ._Amount1 import Amount1

class AgreedAmount1Choice(base_types._BaseFieldType):

	__slots__ = ["_AgrdAmtDtls", "_SgrtdIndpdntAmt"]
	@property
	def AgrdAmtDtls(self):
		return self._AgrdAmtDtls

	@AgrdAmtDtls.setter
	def AgrdAmtDtls(self, value):
		self._AgrdAmtDtls = value if type(value) != base_types.auto else self.make_default("AgrdAmtDtls")

	@AgrdAmtDtls.deleter
	def AgrdAmtDtls(self):
		del self._AgrdAmtDtls
		self._AgrdAmtDtls = None

	@property
	def SgrtdIndpdntAmt(self):
		return self._SgrtdIndpdntAmt

	@SgrtdIndpdntAmt.setter
	def SgrtdIndpdntAmt(self, value):
		self._SgrtdIndpdntAmt = value if type(value) != base_types.auto else self.make_default("SgrtdIndpdntAmt")

	@SgrtdIndpdntAmt.deleter
	def SgrtdIndpdntAmt(self):
		del self._SgrtdIndpdntAmt
		self._SgrtdIndpdntAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AgrdAmtDtls', type=AgreedAmount1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SgrtdIndpdntAmt', type=Amount1, min=0, max=1, mutex_group=1, array=False),
	))