from . import base_types
import Status39Choice
import Transaction127

class StatusAndReason45(base_types._BaseFieldType):

	__slots__ = ["_StsAndRsn", "_Tx"]
	@property
	def StsAndRsn(self):
		return self._StsAndRsn

	@StsAndRsn.setter
	def StsAndRsn(self, value):
		self._StsAndRsn = value if type(value) != auto else self.make_default("StsAndRsn")

	@StsAndRsn.deleter
	def StsAndRsn(self):
		del self._StsAndRsn
		self._StsAndRsn = None

	@property
	def Tx(self):
		return self._Tx

	@Tx.setter
	def Tx(self, value):
		self._Tx = value if type(value) != auto else self.make_default("Tx")

	@Tx.deleter
	def Tx(self):
		del self._Tx
		self._Tx = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='StsAndRsn', type=Status39Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tx', type=Transaction127, min=0, max=None, mutex_group=None, array=True),
	))

