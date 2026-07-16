# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ConfirmationRejectedStatus2
from . import OrderConfirmationStatus1Code

class ConfirmationStatus1Choice(base_types._BaseFieldType):

	__slots__ = ["_AmdmntRjctd", "_ConfRjctd", "_Sts"]
	@property
	def AmdmntRjctd(self):
		return self._AmdmntRjctd

	@AmdmntRjctd.setter
	def AmdmntRjctd(self, value):
		self._AmdmntRjctd = value if value is not None else base_types.UninitialisedField(self, 'AmdmntRjctd', ConfirmationRejectedStatus2, True)

	@AmdmntRjctd.deleter
	def AmdmntRjctd(self):
		del self._AmdmntRjctd
		self._AmdmntRjctd = base_types.UninitialisedField(self, 'AmdmntRjctd', ConfirmationRejectedStatus2, True)

	@property
	def ConfRjctd(self):
		return self._ConfRjctd

	@ConfRjctd.setter
	def ConfRjctd(self, value):
		self._ConfRjctd = value if value is not None else base_types.UninitialisedField(self, 'ConfRjctd', ConfirmationRejectedStatus2, True)

	@ConfRjctd.deleter
	def ConfRjctd(self):
		del self._ConfRjctd
		self._ConfRjctd = base_types.UninitialisedField(self, 'ConfRjctd', ConfirmationRejectedStatus2, True)

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if value is not None else base_types.UninitialisedField(self, 'Sts', OrderConfirmationStatus1Code, False)

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = base_types.UninitialisedField(self, 'Sts', OrderConfirmationStatus1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AmdmntRjctd', type=ConfirmationRejectedStatus2, min=1, max=10, mutex_group=1, array=True),
		base_types.FieldEntry(name='ConfRjctd', type=ConfirmationRejectedStatus2, min=1, max=10, mutex_group=1, array=True),
		base_types.FieldEntry(name='Sts', type=OrderConfirmationStatus1Code, min=0, max=1, mutex_group=1, array=False),
	))