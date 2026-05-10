import base_types
import SupplementaryDataEnvelope1
import InvestigationStatus1Code

class InvestigationResult1Choice(base_types._BaseFieldType):

	__slots__ = ["_Rslt", "_InvstgtnSts"]
	@property
	def Rslt(self):
		return self._Rslt

	@Rslt.setter
	def Rslt(self, value):
		self._Rslt = value if type(value) != auto else self.make_default("Rslt")

	@Rslt.deleter
	def Rslt(self):
		del self._Rslt
		self._Rslt = None

	@property
	def InvstgtnSts(self):
		return self._InvstgtnSts

	@InvstgtnSts.setter
	def InvstgtnSts(self, value):
		self._InvstgtnSts = value if type(value) != auto else self.make_default("InvstgtnSts")

	@InvstgtnSts.deleter
	def InvstgtnSts(self):
		del self._InvstgtnSts
		self._InvstgtnSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Rslt', type=SupplementaryDataEnvelope1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='InvstgtnSts', type=InvestigationStatus1Code, min=0, max=1, mutex_group=1, array=False),
	))

