# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CancelledStatusReason16
from . import ConditionallyAcceptedStatus3Choice
from . import OrderStatus4Code
from . import PartiallySettledStatus10
from . import RejectedStatus9
from . import SuspendedStatusReason4Choice

class OrderStatus3Choice(base_types._BaseFieldType):

	__slots__ = ["_Canc", "_CondlyAccptd", "_PrtlySttld", "_Rjctd", "_Sspd", "_Sts"]
	@property
	def Canc(self):
		return self._Canc

	@Canc.setter
	def Canc(self, value):
		self._Canc = value if value is not None else base_types.UninitialisedField(self, 'Canc', CancelledStatusReason16, False)

	@Canc.deleter
	def Canc(self):
		del self._Canc
		self._Canc = base_types.UninitialisedField(self, 'Canc', CancelledStatusReason16, False)

	@property
	def CondlyAccptd(self):
		return self._CondlyAccptd

	@CondlyAccptd.setter
	def CondlyAccptd(self, value):
		self._CondlyAccptd = value if value is not None else base_types.UninitialisedField(self, 'CondlyAccptd', ConditionallyAcceptedStatus3Choice, False)

	@CondlyAccptd.deleter
	def CondlyAccptd(self):
		del self._CondlyAccptd
		self._CondlyAccptd = base_types.UninitialisedField(self, 'CondlyAccptd', ConditionallyAcceptedStatus3Choice, False)

	@property
	def PrtlySttld(self):
		return self._PrtlySttld

	@PrtlySttld.setter
	def PrtlySttld(self, value):
		self._PrtlySttld = value if value is not None else base_types.UninitialisedField(self, 'PrtlySttld', PartiallySettledStatus10, False)

	@PrtlySttld.deleter
	def PrtlySttld(self):
		del self._PrtlySttld
		self._PrtlySttld = base_types.UninitialisedField(self, 'PrtlySttld', PartiallySettledStatus10, False)

	@property
	def Rjctd(self):
		return self._Rjctd

	@Rjctd.setter
	def Rjctd(self, value):
		self._Rjctd = value if value is not None else base_types.UninitialisedField(self, 'Rjctd', RejectedStatus9, True)

	@Rjctd.deleter
	def Rjctd(self):
		del self._Rjctd
		self._Rjctd = base_types.UninitialisedField(self, 'Rjctd', RejectedStatus9, True)

	@property
	def Sspd(self):
		return self._Sspd

	@Sspd.setter
	def Sspd(self, value):
		self._Sspd = value if value is not None else base_types.UninitialisedField(self, 'Sspd', SuspendedStatusReason4Choice, False)

	@Sspd.deleter
	def Sspd(self):
		del self._Sspd
		self._Sspd = base_types.UninitialisedField(self, 'Sspd', SuspendedStatusReason4Choice, False)

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if value is not None else base_types.UninitialisedField(self, 'Sts', OrderStatus4Code, False)

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = base_types.UninitialisedField(self, 'Sts', OrderStatus4Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Canc', type=CancelledStatusReason16, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CondlyAccptd', type=ConditionallyAcceptedStatus3Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrtlySttld', type=PartiallySettledStatus10, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rjctd', type=RejectedStatus9, min=1, max=10, mutex_group=1, array=True),
		base_types.FieldEntry(name='Sspd', type=SuspendedStatusReason4Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Sts', type=OrderStatus4Code, min=0, max=1, mutex_group=1, array=False),
	))