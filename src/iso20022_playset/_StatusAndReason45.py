# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Status39Choice
from . import Transaction127

class StatusAndReason45(base_types._BaseFieldType):

	__slots__ = ["_StsAndRsn", "_Tx"]
	@property
	def StsAndRsn(self):
		return self._StsAndRsn

	@StsAndRsn.setter
	def StsAndRsn(self, value):
		self._StsAndRsn = value if value is not None else base_types.UninitialisedField(self, 'StsAndRsn', Status39Choice, False)

	@StsAndRsn.deleter
	def StsAndRsn(self):
		del self._StsAndRsn
		self._StsAndRsn = base_types.UninitialisedField(self, 'StsAndRsn', Status39Choice, False)

	@property
	def Tx(self):
		return self._Tx

	@Tx.setter
	def Tx(self, value):
		self._Tx = value if value is not None else base_types.UninitialisedField(self, 'Tx', Transaction127, True)

	@Tx.deleter
	def Tx(self):
		del self._Tx
		self._Tx = base_types.UninitialisedField(self, 'Tx', Transaction127, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='StsAndRsn', type=Status39Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tx', type=Transaction127, min=0, max=None, mutex_group=None, array=True),
	))