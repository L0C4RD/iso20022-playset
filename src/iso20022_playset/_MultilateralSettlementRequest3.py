# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import MovementRecord2
from . import Number
from . import Priority3Code
from . import SettlementTimeRequest2

class MultilateralSettlementRequest3(base_types._BaseFieldType):

	__slots__ = ["_InstrId", "_InstrPrty", "_MvmntRcrd", "_NbOfMvmntRcrds", "_SttlmCycl", "_SttlmPrty", "_SttlmTmReq"]
	@property
	def InstrId(self):
		return self._InstrId

	@InstrId.setter
	def InstrId(self, value):
		self._InstrId = value if value is not None else base_types.UninitialisedField(self, 'InstrId', Max35Text, False)

	@InstrId.deleter
	def InstrId(self):
		del self._InstrId
		self._InstrId = base_types.UninitialisedField(self, 'InstrId', Max35Text, False)

	@property
	def InstrPrty(self):
		return self._InstrPrty

	@InstrPrty.setter
	def InstrPrty(self, value):
		self._InstrPrty = value if value is not None else base_types.UninitialisedField(self, 'InstrPrty', Priority3Code, False)

	@InstrPrty.deleter
	def InstrPrty(self):
		del self._InstrPrty
		self._InstrPrty = base_types.UninitialisedField(self, 'InstrPrty', Priority3Code, False)

	@property
	def MvmntRcrd(self):
		return self._MvmntRcrd

	@MvmntRcrd.setter
	def MvmntRcrd(self, value):
		self._MvmntRcrd = value if value is not None else base_types.UninitialisedField(self, 'MvmntRcrd', MovementRecord2, True)

	@MvmntRcrd.deleter
	def MvmntRcrd(self):
		del self._MvmntRcrd
		self._MvmntRcrd = base_types.UninitialisedField(self, 'MvmntRcrd', MovementRecord2, True)

	@property
	def NbOfMvmntRcrds(self):
		return self._NbOfMvmntRcrds

	@NbOfMvmntRcrds.setter
	def NbOfMvmntRcrds(self, value):
		self._NbOfMvmntRcrds = value if value is not None else base_types.UninitialisedField(self, 'NbOfMvmntRcrds', Number, False)

	@NbOfMvmntRcrds.deleter
	def NbOfMvmntRcrds(self):
		del self._NbOfMvmntRcrds
		self._NbOfMvmntRcrds = base_types.UninitialisedField(self, 'NbOfMvmntRcrds', Number, False)

	@property
	def SttlmCycl(self):
		return self._SttlmCycl

	@SttlmCycl.setter
	def SttlmCycl(self, value):
		self._SttlmCycl = value if value is not None else base_types.UninitialisedField(self, 'SttlmCycl', Max35Text, False)

	@SttlmCycl.deleter
	def SttlmCycl(self):
		del self._SttlmCycl
		self._SttlmCycl = base_types.UninitialisedField(self, 'SttlmCycl', Max35Text, False)

	@property
	def SttlmPrty(self):
		return self._SttlmPrty

	@SttlmPrty.setter
	def SttlmPrty(self, value):
		self._SttlmPrty = value if value is not None else base_types.UninitialisedField(self, 'SttlmPrty', Priority3Code, False)

	@SttlmPrty.deleter
	def SttlmPrty(self):
		del self._SttlmPrty
		self._SttlmPrty = base_types.UninitialisedField(self, 'SttlmPrty', Priority3Code, False)

	@property
	def SttlmTmReq(self):
		return self._SttlmTmReq

	@SttlmTmReq.setter
	def SttlmTmReq(self, value):
		self._SttlmTmReq = value if value is not None else base_types.UninitialisedField(self, 'SttlmTmReq', SettlementTimeRequest2, False)

	@SttlmTmReq.deleter
	def SttlmTmReq(self):
		del self._SttlmTmReq
		self._SttlmTmReq = base_types.UninitialisedField(self, 'SttlmTmReq', SettlementTimeRequest2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='InstrId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrPrty', type=Priority3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MvmntRcrd', type=MovementRecord2, min=2, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NbOfMvmntRcrds', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmCycl', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmPrty', type=Priority3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmTmReq', type=SettlementTimeRequest2, min=0, max=1, mutex_group=None, array=False),
	))