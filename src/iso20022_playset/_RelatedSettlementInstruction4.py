# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import UTIIdentifier

class RelatedSettlementInstruction4(base_types._BaseFieldType):

	__slots__ = ["_MktInfrstrctrTxId", "_PrcrTxId", "_RltdSttlmInstrId", "_UnqTxIdr"]
	@property
	def MktInfrstrctrTxId(self):
		return self._MktInfrstrctrTxId

	@MktInfrstrctrTxId.setter
	def MktInfrstrctrTxId(self, value):
		self._MktInfrstrctrTxId = value if value is not None else base_types.UninitialisedField(self, 'MktInfrstrctrTxId', Max35Text, False)

	@MktInfrstrctrTxId.deleter
	def MktInfrstrctrTxId(self):
		del self._MktInfrstrctrTxId
		self._MktInfrstrctrTxId = base_types.UninitialisedField(self, 'MktInfrstrctrTxId', Max35Text, False)

	@property
	def PrcrTxId(self):
		return self._PrcrTxId

	@PrcrTxId.setter
	def PrcrTxId(self, value):
		self._PrcrTxId = value if value is not None else base_types.UninitialisedField(self, 'PrcrTxId', Max35Text, False)

	@PrcrTxId.deleter
	def PrcrTxId(self):
		del self._PrcrTxId
		self._PrcrTxId = base_types.UninitialisedField(self, 'PrcrTxId', Max35Text, False)

	@property
	def RltdSttlmInstrId(self):
		return self._RltdSttlmInstrId

	@RltdSttlmInstrId.setter
	def RltdSttlmInstrId(self, value):
		self._RltdSttlmInstrId = value if value is not None else base_types.UninitialisedField(self, 'RltdSttlmInstrId', Max35Text, False)

	@RltdSttlmInstrId.deleter
	def RltdSttlmInstrId(self):
		del self._RltdSttlmInstrId
		self._RltdSttlmInstrId = base_types.UninitialisedField(self, 'RltdSttlmInstrId', Max35Text, False)

	@property
	def UnqTxIdr(self):
		return self._UnqTxIdr

	@UnqTxIdr.setter
	def UnqTxIdr(self, value):
		self._UnqTxIdr = value if value is not None else base_types.UninitialisedField(self, 'UnqTxIdr', UTIIdentifier, False)

	@UnqTxIdr.deleter
	def UnqTxIdr(self):
		del self._UnqTxIdr
		self._UnqTxIdr = base_types.UninitialisedField(self, 'UnqTxIdr', UTIIdentifier, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='MktInfrstrctrTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcrTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdSttlmInstrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnqTxIdr', type=UTIIdentifier, min=0, max=1, mutex_group=None, array=False),
	))