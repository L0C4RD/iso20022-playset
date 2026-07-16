# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import Max140Text
from . import Max35Text
from . import RejectionReason68Code

class CollateralSubstitutionResponse3(base_types._BaseFieldType):

	__slots__ = ["_CollSbstitnReqId", "_RjctdAmt", "_RjctnRsn", "_RjctnRsnInf"]
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

	@property
	def RjctdAmt(self):
		return self._RjctdAmt

	@RjctdAmt.setter
	def RjctdAmt(self, value):
		self._RjctdAmt = value if value is not None else base_types.UninitialisedField(self, 'RjctdAmt', ActiveCurrencyAndAmount, False)

	@RjctdAmt.deleter
	def RjctdAmt(self):
		del self._RjctdAmt
		self._RjctdAmt = base_types.UninitialisedField(self, 'RjctdAmt', ActiveCurrencyAndAmount, False)

	@property
	def RjctnRsn(self):
		return self._RjctnRsn

	@RjctnRsn.setter
	def RjctnRsn(self, value):
		self._RjctnRsn = value if value is not None else base_types.UninitialisedField(self, 'RjctnRsn', RejectionReason68Code, False)

	@RjctnRsn.deleter
	def RjctnRsn(self):
		del self._RjctnRsn
		self._RjctnRsn = base_types.UninitialisedField(self, 'RjctnRsn', RejectionReason68Code, False)

	@property
	def RjctnRsnInf(self):
		return self._RjctnRsnInf

	@RjctnRsnInf.setter
	def RjctnRsnInf(self, value):
		self._RjctnRsnInf = value if value is not None else base_types.UninitialisedField(self, 'RjctnRsnInf', Max140Text, False)

	@RjctnRsnInf.deleter
	def RjctnRsnInf(self):
		del self._RjctnRsnInf
		self._RjctnRsnInf = base_types.UninitialisedField(self, 'RjctnRsnInf', Max140Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollSbstitnReqId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RjctdAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RjctnRsn', type=RejectionReason68Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RjctnRsnInf', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
	))