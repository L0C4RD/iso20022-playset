# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODateTime
from . import PaymentType4Choice

class PaymentInstruction13(base_types._BaseFieldType):

	__slots__ = ["_PmtTp", "_ReqdExctnDtTm"]
	@property
	def PmtTp(self):
		return self._PmtTp

	@PmtTp.setter
	def PmtTp(self, value):
		self._PmtTp = value if value is not None else base_types.UninitialisedField(self, 'PmtTp', PaymentType4Choice, False)

	@PmtTp.deleter
	def PmtTp(self):
		del self._PmtTp
		self._PmtTp = base_types.UninitialisedField(self, 'PmtTp', PaymentType4Choice, False)

	@property
	def ReqdExctnDtTm(self):
		return self._ReqdExctnDtTm

	@ReqdExctnDtTm.setter
	def ReqdExctnDtTm(self, value):
		self._ReqdExctnDtTm = value if value is not None else base_types.UninitialisedField(self, 'ReqdExctnDtTm', ISODateTime, False)

	@ReqdExctnDtTm.deleter
	def ReqdExctnDtTm(self):
		del self._ReqdExctnDtTm
		self._ReqdExctnDtTm = base_types.UninitialisedField(self, 'ReqdExctnDtTm', ISODateTime, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='PmtTp', type=PaymentType4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdExctnDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
	))