import base_types
import CollateralType21
import TrueFalseIndicator
import SecurityIdentification26Choice

class CollateralData35(base_types._BaseFieldType):

	__slots__ = ["_AsstTp", "_NetXpsrCollstnInd", "_BsktIdr"]
	@property
	def AsstTp(self):
		return self._AsstTp

	@AsstTp.setter
	def AsstTp(self, value):
		self._AsstTp = value if type(value) != auto else self.make_default("AsstTp")

	@AsstTp.deleter
	def AsstTp(self):
		del self._AsstTp
		self._AsstTp = None

	@property
	def NetXpsrCollstnInd(self):
		return self._NetXpsrCollstnInd

	@NetXpsrCollstnInd.setter
	def NetXpsrCollstnInd(self, value):
		self._NetXpsrCollstnInd = value if type(value) != auto else self.make_default("NetXpsrCollstnInd")

	@NetXpsrCollstnInd.deleter
	def NetXpsrCollstnInd(self):
		del self._NetXpsrCollstnInd
		self._NetXpsrCollstnInd = None

	@property
	def BsktIdr(self):
		return self._BsktIdr

	@BsktIdr.setter
	def BsktIdr(self, value):
		self._BsktIdr = value if type(value) != auto else self.make_default("BsktIdr")

	@BsktIdr.deleter
	def BsktIdr(self):
		del self._BsktIdr
		self._BsktIdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AsstTp', type=CollateralType21, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetXpsrCollstnInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BsktIdr', type=SecurityIdentification26Choice, min=0, max=1, mutex_group=None, array=False),
	))

