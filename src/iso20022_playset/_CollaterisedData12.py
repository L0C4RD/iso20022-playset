from . import base_types
from .TrueFalseIndicator import TrueFalseIndicator
from .SecurityIdentification26Choice import SecurityIdentification26Choice
from .CollateralType21 import CollateralType21
from .ISODate import ISODate

class CollaterisedData12(base_types._BaseFieldType):

	__slots__ = ["_AsstTp", "_BsktIdr", "_CollValDt", "_NetXpsrCollstnInd"]
	@property
	def AsstTp(self):
		return self._AsstTp

	@AsstTp.setter
	def AsstTp(self, value):
		self._AsstTp = value if type(value) != base_types.auto else self.make_default("AsstTp")

	@AsstTp.deleter
	def AsstTp(self):
		del self._AsstTp
		self._AsstTp = None

	@property
	def BsktIdr(self):
		return self._BsktIdr

	@BsktIdr.setter
	def BsktIdr(self, value):
		self._BsktIdr = value if type(value) != base_types.auto else self.make_default("BsktIdr")

	@BsktIdr.deleter
	def BsktIdr(self):
		del self._BsktIdr
		self._BsktIdr = None

	@property
	def CollValDt(self):
		return self._CollValDt

	@CollValDt.setter
	def CollValDt(self, value):
		self._CollValDt = value if type(value) != base_types.auto else self.make_default("CollValDt")

	@CollValDt.deleter
	def CollValDt(self):
		del self._CollValDt
		self._CollValDt = None

	@property
	def NetXpsrCollstnInd(self):
		return self._NetXpsrCollstnInd

	@NetXpsrCollstnInd.setter
	def NetXpsrCollstnInd(self, value):
		self._NetXpsrCollstnInd = value if type(value) != base_types.auto else self.make_default("NetXpsrCollstnInd")

	@NetXpsrCollstnInd.deleter
	def NetXpsrCollstnInd(self):
		del self._NetXpsrCollstnInd
		self._NetXpsrCollstnInd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AsstTp', type=CollateralType21, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BsktIdr', type=SecurityIdentification26Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollValDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetXpsrCollstnInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
	))

