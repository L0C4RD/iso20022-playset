# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CashAccount204 import CashAccount204
from ._DataModification2Code import DataModification2Code
from ._PaymentInstrument17 import PaymentInstrument17

class CashSettlement4(base_types._BaseFieldType):

	__slots__ = ["_CshAcctDtls", "_ModScpIndctn", "_OthrCshSttlmDtls"]
	@property
	def CshAcctDtls(self):
		return self._CshAcctDtls

	@CshAcctDtls.setter
	def CshAcctDtls(self, value):
		self._CshAcctDtls = value if type(value) != base_types.auto else self.make_default("CshAcctDtls")

	@CshAcctDtls.deleter
	def CshAcctDtls(self):
		del self._CshAcctDtls
		self._CshAcctDtls = None

	@property
	def ModScpIndctn(self):
		return self._ModScpIndctn

	@ModScpIndctn.setter
	def ModScpIndctn(self, value):
		self._ModScpIndctn = value if type(value) != base_types.auto else self.make_default("ModScpIndctn")

	@ModScpIndctn.deleter
	def ModScpIndctn(self):
		del self._ModScpIndctn
		self._ModScpIndctn = None

	@property
	def OthrCshSttlmDtls(self):
		return self._OthrCshSttlmDtls

	@OthrCshSttlmDtls.setter
	def OthrCshSttlmDtls(self, value):
		self._OthrCshSttlmDtls = value if type(value) != base_types.auto else self.make_default("OthrCshSttlmDtls")

	@OthrCshSttlmDtls.deleter
	def OthrCshSttlmDtls(self):
		del self._OthrCshSttlmDtls
		self._OthrCshSttlmDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CshAcctDtls', type=CashAccount204, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ModScpIndctn', type=DataModification2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrCshSttlmDtls', type=PaymentInstrument17, min=0, max=None, mutex_group=None, array=True),
	))