from . import base_types
import PendingStatus46Choice
import ProprietaryStatusAndReason7
import RejectionOrRepairStatus46Choice
import ProprietaryReason5
import AcknowledgedAcceptedStatus25Choice
import DeniedStatus19Choice

class ProcessingStatus91Choice(base_types._BaseFieldType):

	__slots__ = ["_Cmpltd", "_Rjctd", "_Prtry", "_AckdAccptd", "_Pdg", "_Dnd"]
	@property
	def Cmpltd(self):
		return self._Cmpltd

	@Cmpltd.setter
	def Cmpltd(self, value):
		self._Cmpltd = value if type(value) != auto else self.make_default("Cmpltd")

	@Cmpltd.deleter
	def Cmpltd(self):
		del self._Cmpltd
		self._Cmpltd = None

	@property
	def Rjctd(self):
		return self._Rjctd

	@Rjctd.setter
	def Rjctd(self, value):
		self._Rjctd = value if type(value) != auto else self.make_default("Rjctd")

	@Rjctd.deleter
	def Rjctd(self):
		del self._Rjctd
		self._Rjctd = None

	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if type(value) != auto else self.make_default("Prtry")

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = None

	@property
	def AckdAccptd(self):
		return self._AckdAccptd

	@AckdAccptd.setter
	def AckdAccptd(self, value):
		self._AckdAccptd = value if type(value) != auto else self.make_default("AckdAccptd")

	@AckdAccptd.deleter
	def AckdAccptd(self):
		del self._AckdAccptd
		self._AckdAccptd = None

	@property
	def Pdg(self):
		return self._Pdg

	@Pdg.setter
	def Pdg(self, value):
		self._Pdg = value if type(value) != auto else self.make_default("Pdg")

	@Pdg.deleter
	def Pdg(self):
		del self._Pdg
		self._Pdg = None

	@property
	def Dnd(self):
		return self._Dnd

	@Dnd.setter
	def Dnd(self, value):
		self._Dnd = value if type(value) != auto else self.make_default("Dnd")

	@Dnd.deleter
	def Dnd(self):
		del self._Dnd
		self._Dnd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cmpltd', type=ProprietaryReason5, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rjctd', type=RejectionOrRepairStatus46Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtry', type=ProprietaryStatusAndReason7, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AckdAccptd', type=AcknowledgedAcceptedStatus25Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Pdg', type=PendingStatus46Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Dnd', type=DeniedStatus19Choice, min=0, max=1, mutex_group=1, array=False),
	))

