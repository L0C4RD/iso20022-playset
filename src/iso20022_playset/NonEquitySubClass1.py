import base_types
import NonEquitySubClassSegmentationCriterion1
import Max1000Text

class NonEquitySubClass1(base_types._BaseFieldType):

	__slots__ = ["_Desc", "_SgmttnCrit"]
	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if type(value) != auto else self.make_default("Desc")

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = None

	@property
	def SgmttnCrit(self):
		return self._SgmttnCrit

	@SgmttnCrit.setter
	def SgmttnCrit(self, value):
		self._SgmttnCrit = value if type(value) != auto else self.make_default("SgmttnCrit")

	@SgmttnCrit.deleter
	def SgmttnCrit(self):
		del self._SgmttnCrit
		self._SgmttnCrit = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Desc', type=Max1000Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SgmttnCrit', type=NonEquitySubClassSegmentationCriterion1, min=1, max=None, mutex_group=None, array=True),
	))

