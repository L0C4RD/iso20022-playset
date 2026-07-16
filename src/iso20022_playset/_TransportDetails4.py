# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Charge25
from . import Consignment3
from . import DocumentIdentification7
from . import Incoterms4
from . import ShipmentDate1Choice
from . import TransportMeans6
from . import TransportedGoods1

class TransportDetails4(base_types._BaseFieldType):

	__slots__ = ["_Consgnmt", "_FrghtChrgs", "_Incotrms", "_RtgSummry", "_ShipmntDt", "_TrnsprtDocRef", "_TrnsprtdGoods"]
	@property
	def Consgnmt(self):
		return self._Consgnmt

	@Consgnmt.setter
	def Consgnmt(self, value):
		self._Consgnmt = value if value is not None else base_types.UninitialisedField(self, 'Consgnmt', Consignment3, False)

	@Consgnmt.deleter
	def Consgnmt(self):
		del self._Consgnmt
		self._Consgnmt = base_types.UninitialisedField(self, 'Consgnmt', Consignment3, False)

	@property
	def FrghtChrgs(self):
		return self._FrghtChrgs

	@FrghtChrgs.setter
	def FrghtChrgs(self, value):
		self._FrghtChrgs = value if value is not None else base_types.UninitialisedField(self, 'FrghtChrgs', Charge25, False)

	@FrghtChrgs.deleter
	def FrghtChrgs(self):
		del self._FrghtChrgs
		self._FrghtChrgs = base_types.UninitialisedField(self, 'FrghtChrgs', Charge25, False)

	@property
	def Incotrms(self):
		return self._Incotrms

	@Incotrms.setter
	def Incotrms(self, value):
		self._Incotrms = value if value is not None else base_types.UninitialisedField(self, 'Incotrms', Incoterms4, False)

	@Incotrms.deleter
	def Incotrms(self):
		del self._Incotrms
		self._Incotrms = base_types.UninitialisedField(self, 'Incotrms', Incoterms4, False)

	@property
	def RtgSummry(self):
		return self._RtgSummry

	@RtgSummry.setter
	def RtgSummry(self, value):
		self._RtgSummry = value if value is not None else base_types.UninitialisedField(self, 'RtgSummry', TransportMeans6, False)

	@RtgSummry.deleter
	def RtgSummry(self):
		del self._RtgSummry
		self._RtgSummry = base_types.UninitialisedField(self, 'RtgSummry', TransportMeans6, False)

	@property
	def ShipmntDt(self):
		return self._ShipmntDt

	@ShipmntDt.setter
	def ShipmntDt(self, value):
		self._ShipmntDt = value if value is not None else base_types.UninitialisedField(self, 'ShipmntDt', ShipmentDate1Choice, False)

	@ShipmntDt.deleter
	def ShipmntDt(self):
		del self._ShipmntDt
		self._ShipmntDt = base_types.UninitialisedField(self, 'ShipmntDt', ShipmentDate1Choice, False)

	@property
	def TrnsprtDocRef(self):
		return self._TrnsprtDocRef

	@TrnsprtDocRef.setter
	def TrnsprtDocRef(self, value):
		self._TrnsprtDocRef = value if value is not None else base_types.UninitialisedField(self, 'TrnsprtDocRef', DocumentIdentification7, True)

	@TrnsprtDocRef.deleter
	def TrnsprtDocRef(self):
		del self._TrnsprtDocRef
		self._TrnsprtDocRef = base_types.UninitialisedField(self, 'TrnsprtDocRef', DocumentIdentification7, True)

	@property
	def TrnsprtdGoods(self):
		return self._TrnsprtdGoods

	@TrnsprtdGoods.setter
	def TrnsprtdGoods(self, value):
		self._TrnsprtdGoods = value if value is not None else base_types.UninitialisedField(self, 'TrnsprtdGoods', TransportedGoods1, True)

	@TrnsprtdGoods.deleter
	def TrnsprtdGoods(self):
		del self._TrnsprtdGoods
		self._TrnsprtdGoods = base_types.UninitialisedField(self, 'TrnsprtdGoods', TransportedGoods1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Consgnmt', type=Consignment3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrghtChrgs', type=Charge25, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Incotrms', type=Incoterms4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtgSummry', type=TransportMeans6, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShipmntDt', type=ShipmentDate1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrnsprtDocRef', type=DocumentIdentification7, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TrnsprtdGoods', type=TransportedGoods1, min=1, max=None, mutex_group=None, array=True),
	))