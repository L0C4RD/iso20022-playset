from . import base_types
from ._Max35Text import Max35Text
from ._CollateralResponse3 import CollateralResponse3
from ._CollateralProposalResponse1Code import CollateralProposalResponse1Code

class CollateralProposalResponseType4(base_types._BaseFieldType):

	__slots__ = ["_Rspn", "_Tp", "_CollPrpslId"]
	@property
	def Rspn(self):
		return self._Rspn

	@Rspn.setter
	def Rspn(self, value):
		self._Rspn = value if type(value) != base_types.auto else self.make_default("Rspn")

	@Rspn.deleter
	def Rspn(self):
		del self._Rspn
		self._Rspn = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def CollPrpslId(self):
		return self._CollPrpslId

	@CollPrpslId.setter
	def CollPrpslId(self, value):
		self._CollPrpslId = value if type(value) != base_types.auto else self.make_default("CollPrpslId")

	@CollPrpslId.deleter
	def CollPrpslId(self):
		del self._CollPrpslId
		self._CollPrpslId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Rspn', type=CollateralResponse3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=CollateralProposalResponse1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollPrpslId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

