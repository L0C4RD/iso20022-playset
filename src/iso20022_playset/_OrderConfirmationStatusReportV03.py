# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Extension1
from . import IndividualOrderConfirmationStatusAndReason3
from . import MessageIdentification1
from . import References64Choice

class OrderConfirmationStatusReportV03(base_types._BaseFieldType):

	__slots__ = ["_IndvOrdrConfDtlsRpt", "_MsgId", "_Ref", "_Xtnsn"]
	@property
	def IndvOrdrConfDtlsRpt(self):
		return self._IndvOrdrConfDtlsRpt

	@IndvOrdrConfDtlsRpt.setter
	def IndvOrdrConfDtlsRpt(self, value):
		self._IndvOrdrConfDtlsRpt = value if value is not None else base_types.UninitialisedField(self, 'IndvOrdrConfDtlsRpt', IndividualOrderConfirmationStatusAndReason3, True)

	@IndvOrdrConfDtlsRpt.deleter
	def IndvOrdrConfDtlsRpt(self):
		del self._IndvOrdrConfDtlsRpt
		self._IndvOrdrConfDtlsRpt = base_types.UninitialisedField(self, 'IndvOrdrConfDtlsRpt', IndividualOrderConfirmationStatusAndReason3, True)

	@property
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if value is not None else base_types.UninitialisedField(self, 'MsgId', MessageIdentification1, False)

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = base_types.UninitialisedField(self, 'MsgId', MessageIdentification1, False)

	@property
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if value is not None else base_types.UninitialisedField(self, 'Ref', References64Choice, False)

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = base_types.UninitialisedField(self, 'Ref', References64Choice, False)

	@property
	def Xtnsn(self):
		return self._Xtnsn

	@Xtnsn.setter
	def Xtnsn(self, value):
		self._Xtnsn = value if value is not None else base_types.UninitialisedField(self, 'Xtnsn', Extension1, True)

	@Xtnsn.deleter
	def Xtnsn(self):
		del self._Xtnsn
		self._Xtnsn = base_types.UninitialisedField(self, 'Xtnsn', Extension1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='IndvOrdrConfDtlsRpt', type=IndividualOrderConfirmationStatusAndReason3, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MsgId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ref', type=References64Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Xtnsn', type=Extension1, min=0, max=None, mutex_group=None, array=True),
	))