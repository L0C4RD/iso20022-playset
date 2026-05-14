# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Max35Text import Max35Text
from ._MovementRecord2 import MovementRecord2
from ._Number import Number
from ._Priority3Code import Priority3Code
from ._SettlementTimeRequest2 import SettlementTimeRequest2

class MultilateralSettlementRequest3(base_types._BaseFieldType):

	__slots__ = ["_InstrId", "_InstrPrty", "_MvmntRcrd", "_NbOfMvmntRcrds", "_SttlmCycl", "_SttlmPrty", "_SttlmTmReq"]
	@property
	def InstrId(self):
		return self._InstrId

	@InstrId.setter
	def InstrId(self, value):
		self._InstrId = value if type(value) != base_types.auto else self.make_default("InstrId")

	@InstrId.deleter
	def InstrId(self):
		del self._InstrId
		self._InstrId = None

	@property
	def InstrPrty(self):
		return self._InstrPrty

	@InstrPrty.setter
	def InstrPrty(self, value):
		self._InstrPrty = value if type(value) != base_types.auto else self.make_default("InstrPrty")

	@InstrPrty.deleter
	def InstrPrty(self):
		del self._InstrPrty
		self._InstrPrty = None

	@property
	def MvmntRcrd(self):
		return self._MvmntRcrd

	@MvmntRcrd.setter
	def MvmntRcrd(self, value):
		self._MvmntRcrd = value if type(value) != base_types.auto else self.make_default("MvmntRcrd")

	@MvmntRcrd.deleter
	def MvmntRcrd(self):
		del self._MvmntRcrd
		self._MvmntRcrd = None

	@property
	def NbOfMvmntRcrds(self):
		return self._NbOfMvmntRcrds

	@NbOfMvmntRcrds.setter
	def NbOfMvmntRcrds(self, value):
		self._NbOfMvmntRcrds = value if type(value) != base_types.auto else self.make_default("NbOfMvmntRcrds")

	@NbOfMvmntRcrds.deleter
	def NbOfMvmntRcrds(self):
		del self._NbOfMvmntRcrds
		self._NbOfMvmntRcrds = None

	@property
	def SttlmCycl(self):
		return self._SttlmCycl

	@SttlmCycl.setter
	def SttlmCycl(self, value):
		self._SttlmCycl = value if type(value) != base_types.auto else self.make_default("SttlmCycl")

	@SttlmCycl.deleter
	def SttlmCycl(self):
		del self._SttlmCycl
		self._SttlmCycl = None

	@property
	def SttlmPrty(self):
		return self._SttlmPrty

	@SttlmPrty.setter
	def SttlmPrty(self, value):
		self._SttlmPrty = value if type(value) != base_types.auto else self.make_default("SttlmPrty")

	@SttlmPrty.deleter
	def SttlmPrty(self):
		del self._SttlmPrty
		self._SttlmPrty = None

	@property
	def SttlmTmReq(self):
		return self._SttlmTmReq

	@SttlmTmReq.setter
	def SttlmTmReq(self, value):
		self._SttlmTmReq = value if type(value) != base_types.auto else self.make_default("SttlmTmReq")

	@SttlmTmReq.deleter
	def SttlmTmReq(self):
		del self._SttlmTmReq
		self._SttlmTmReq = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='InstrId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrPrty', type=Priority3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MvmntRcrd', type=MovementRecord2, min=2, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NbOfMvmntRcrds', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmCycl', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmPrty', type=Priority3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmTmReq', type=SettlementTimeRequest2, min=0, max=1, mutex_group=None, array=False),
	))