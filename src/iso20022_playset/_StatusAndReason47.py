# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Status38Choice
from . import Transaction162

class StatusAndReason47(base_types._BaseFieldType):

	__slots__ = ["_StsAndRsn", "_Tx"]
	@property
	def StsAndRsn(self):
		return self._StsAndRsn

	@StsAndRsn.setter
	def StsAndRsn(self, value):
		self._StsAndRsn = value if value is not None else base_types.UninitialisedField(self, 'StsAndRsn', Status38Choice, False)

	@StsAndRsn.deleter
	def StsAndRsn(self):
		del self._StsAndRsn
		self._StsAndRsn = base_types.UninitialisedField(self, 'StsAndRsn', Status38Choice, False)

	@property
	def Tx(self):
		return self._Tx

	@Tx.setter
	def Tx(self, value):
		self._Tx = value if value is not None else base_types.UninitialisedField(self, 'Tx', Transaction162, True)

	@Tx.deleter
	def Tx(self):
		del self._Tx
		self._Tx = base_types.UninitialisedField(self, 'Tx', Transaction162, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='StsAndRsn', type=Status38Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tx', type=Transaction162, min=0, max=None, mutex_group=None, array=True),
	))