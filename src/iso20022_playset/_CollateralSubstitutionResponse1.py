# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import Max35Text

class CollateralSubstitutionResponse1(base_types._BaseFieldType):

	__slots__ = ["_AccptdAmt", "_CollSbstitnReqId"]
	@property
	def AccptdAmt(self):
		return self._AccptdAmt

	@AccptdAmt.setter
	def AccptdAmt(self, value):
		self._AccptdAmt = value if value is not None else base_types.UninitialisedField(self, 'AccptdAmt', ActiveCurrencyAndAmount, False)

	@AccptdAmt.deleter
	def AccptdAmt(self):
		del self._AccptdAmt
		self._AccptdAmt = base_types.UninitialisedField(self, 'AccptdAmt', ActiveCurrencyAndAmount, False)

	@property
	def CollSbstitnReqId(self):
		return self._CollSbstitnReqId

	@CollSbstitnReqId.setter
	def CollSbstitnReqId(self, value):
		self._CollSbstitnReqId = value if value is not None else base_types.UninitialisedField(self, 'CollSbstitnReqId', Max35Text, False)

	@CollSbstitnReqId.deleter
	def CollSbstitnReqId(self):
		del self._CollSbstitnReqId
		self._CollSbstitnReqId = base_types.UninitialisedField(self, 'CollSbstitnReqId', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AccptdAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollSbstitnReqId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))