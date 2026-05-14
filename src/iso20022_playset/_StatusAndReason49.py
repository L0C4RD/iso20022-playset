# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Status43Choice import Status43Choice
from ._Transaction166 import Transaction166

class StatusAndReason49(base_types._BaseFieldType):

	__slots__ = ["_StsAndRsn", "_Tx"]
	@property
	def StsAndRsn(self):
		return self._StsAndRsn

	@StsAndRsn.setter
	def StsAndRsn(self, value):
		self._StsAndRsn = value if type(value) != base_types.auto else self.make_default("StsAndRsn")

	@StsAndRsn.deleter
	def StsAndRsn(self):
		del self._StsAndRsn
		self._StsAndRsn = None

	@property
	def Tx(self):
		return self._Tx

	@Tx.setter
	def Tx(self, value):
		self._Tx = value if type(value) != base_types.auto else self.make_default("Tx")

	@Tx.deleter
	def Tx(self):
		del self._Tx
		self._Tx = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='StsAndRsn', type=Status43Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tx', type=Transaction166, min=0, max=None, mutex_group=None, array=True),
	))