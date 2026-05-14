# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AcknowledgedAcceptedStatus25Choice import AcknowledgedAcceptedStatus25Choice
from ._CancellationStatus25Choice import CancellationStatus25Choice
from ._ProprietaryStatusAndReason7 import ProprietaryStatusAndReason7
from ._RejectionOrRepairStatus45Choice import RejectionOrRepairStatus45Choice

class IntraPositionProcessingStatus10Choice(base_types._BaseFieldType):

	__slots__ = ["_AckdAccptd", "_Canc", "_Prtry", "_Rjctd", "_Rpr"]
	@property
	def AckdAccptd(self):
		return self._AckdAccptd

	@AckdAccptd.setter
	def AckdAccptd(self, value):
		self._AckdAccptd = value if type(value) != base_types.auto else self.make_default("AckdAccptd")

	@AckdAccptd.deleter
	def AckdAccptd(self):
		del self._AckdAccptd
		self._AckdAccptd = None

	@property
	def Canc(self):
		return self._Canc

	@Canc.setter
	def Canc(self, value):
		self._Canc = value if type(value) != base_types.auto else self.make_default("Canc")

	@Canc.deleter
	def Canc(self):
		del self._Canc
		self._Canc = None

	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if type(value) != base_types.auto else self.make_default("Prtry")

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = None

	@property
	def Rjctd(self):
		return self._Rjctd

	@Rjctd.setter
	def Rjctd(self, value):
		self._Rjctd = value if type(value) != base_types.auto else self.make_default("Rjctd")

	@Rjctd.deleter
	def Rjctd(self):
		del self._Rjctd
		self._Rjctd = None

	@property
	def Rpr(self):
		return self._Rpr

	@Rpr.setter
	def Rpr(self, value):
		self._Rpr = value if type(value) != base_types.auto else self.make_default("Rpr")

	@Rpr.deleter
	def Rpr(self):
		del self._Rpr
		self._Rpr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AckdAccptd', type=AcknowledgedAcceptedStatus25Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Canc', type=CancellationStatus25Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtry', type=ProprietaryStatusAndReason7, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rjctd', type=RejectionOrRepairStatus45Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rpr', type=RejectionOrRepairStatus45Choice, min=0, max=1, mutex_group=1, array=False),
	))